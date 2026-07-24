#!/usr/bin/env python3
"""
transcribe_all.py — batch-transcribe every reference reel with ONE model load.

Loading faster-whisper large-v3 costs ~15s; doing it per video wastes minutes.
This loads once and walks the whole corpus, writing per-video transcripts into
_work/<stem>/ and merging the result into that video's analysis.json.

Resumable: a video that already has transcript.json is skipped unless --force.

Usage:
  python transcribe_all.py [--raw DIR] [--work DIR] [--lang ru]
                           [--model large-v3] [--threads 4] [--force]

NOTE: cpu_threads must stay low (4). Higher values make MKL request allocations
that fail on this machine ("mkl_malloc: failed to allocate memory").
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

VIDEO_EXT = {".mp4", ".mov", ".webm", ".mkv", ".m4v"}


def main():
    here = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=str(here / "referens-reels-hook" / "raw"))
    ap.add_argument("--work", default=str(here / "referens-reels-hook" / "_work"))
    ap.add_argument("--lang", default="ru")
    ap.add_argument("--model", default="large-v3")
    ap.add_argument("--threads", type=int, default=4)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    raw, work = Path(args.raw), Path(args.work)
    vids = sorted(p for p in raw.iterdir() if p.suffix.lower() in VIDEO_EXT)
    if not vids:
        sys.exit(f"no videos in {raw}")

    todo = []
    for v in vids:
        out = work / v.stem
        if not args.force and (out / "transcript.json").exists():
            print(f"[skip] {v.name} (already transcribed)", flush=True)
            continue
        todo.append(v)
    if not todo:
        print("[done] nothing to do")
        return

    from faster_whisper import WhisperModel
    print(f"[load] {args.model} int8 threads={args.threads} ...", flush=True)
    t0 = time.time()
    model = WhisperModel(args.model, device="cpu", compute_type="int8",
                         cpu_threads=args.threads)
    print(f"[load] ready in {time.time() - t0:.1f}s · {len(todo)} videos queued", flush=True)

    for i, v in enumerate(todo, 1):
        out = work / v.stem
        out.mkdir(parents=True, exist_ok=True)
        t1 = time.time()
        try:
            segments, info = model.transcribe(
                str(v), language=args.lang, word_timestamps=True,
                vad_filter=True, beam_size=5, condition_on_previous_text=False)
            segs, words, lines = [], [], []
            for s in segments:
                segs.append({"start": round(s.start, 2), "end": round(s.end, 2),
                             "text": s.text.strip()})
                lines.append(f"{s.start:7.2f}–{s.end:7.2f}  {s.text.strip()}")
                for w in (s.words or []):
                    words.append({"t": round(w.start, 2), "w": w.word.strip()})
            (out / "transcript.txt").write_text("\n".join(lines), encoding="utf-8")
            (out / "transcript_plain.txt").write_text(
                " ".join(s["text"] for s in segs), encoding="utf-8")
            (out / "transcript.json").write_text(
                json.dumps({"segments": segs, "words": words},
                           ensure_ascii=False, indent=2), encoding="utf-8")

            aj = out / "analysis.json"
            summary = json.loads(aj.read_text(encoding="utf-8")) if aj.exists() else {}
            summary["transcript"] = {"language": info.language,
                                     "language_prob": round(info.language_probability, 2),
                                     "n_segments": len(segs), "n_words": len(words)}
            aj.write_text(json.dumps(summary, ensure_ascii=False, indent=2),
                          encoding="utf-8")
            print(f"[{i}/{len(todo)}] {v.name}  {time.time() - t1:.0f}s  "
                  f"segments={len(segs)} words={len(words)}", flush=True)
        except Exception as e:
            print(f"[{i}/{len(todo)}] ERROR {v.name}: {e}", flush=True)

    print("[done] all transcriptions finished", flush=True)


if __name__ == "__main__":
    main()
