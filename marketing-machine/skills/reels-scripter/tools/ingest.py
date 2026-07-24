#!/usr/bin/env python3
"""
ingest.py — Deep reference-reel ingest for reels-scripter.

Turns one reference video into everything needed to reverse-engineer its formula:

  meta          duration, fps, resolution, audio presence
  cuts          hard-cut timestamps at several sensitivities + cadence stats
  sheets/       TIMESTAMPED contact sheets (1 thumb per second, second burned in)
                -> the montage map; correlate any moment with the transcript
  hook/         first N seconds at high density and high res (the formula's core)
  cuts/         one readable frame immediately after every detected cut
  transcript.*  word-for-word Uzbek transcript with per-segment timestamps

Frame work is fast; transcription is slow. Use --frames-only / --transcribe-only
to run them separately (e.g. frames in foreground, transcription in background).

Usage:
  python ingest.py <video> [--frames-only|--transcribe-only] [--model large-v3]
"""
import argparse
import json
import math
import re
import subprocess
import sys
from pathlib import Path

FONT = "C\\:/Windows/Fonts/arialbd.ttf"   # ffmpeg filter-escaped Windows path


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def ffprobe_meta(video: Path) -> dict:
    r = run(["ffprobe", "-v", "quiet", "-print_format", "json",
             "-show_format", "-show_streams", str(video)])
    if r.returncode != 0:
        raise RuntimeError(f"ffprobe failed: {r.stderr[:400]}")
    data = json.loads(r.stdout)
    v = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), {})
    a = next((s for s in data.get("streams", []) if s.get("codec_type") == "audio"), None)
    fps = 0.0
    if "/" in (v.get("r_frame_rate") or ""):
        n, d = v["r_frame_rate"].split("/")
        fps = float(n) / float(d) if float(d) else 0.0
    dur = float(data.get("format", {}).get("duration") or 0)
    return {"duration_s": round(dur, 2), "fps": round(fps, 2),
            "width": v.get("width"), "height": v.get("height"),
            "has_audio": a is not None,
            "vertical": (v.get("height") or 0) > (v.get("width") or 0)}


def scene_cuts(video: Path, threshold: float) -> list:
    r = run(["ffmpeg", "-i", str(video), "-filter:v",
             f"select='gt(scene,{threshold})',showinfo", "-f", "null", "-"])
    return sorted({round(float(m.group(1)), 2)
                   for m in re.finditer(r"pts_time:([0-9.]+)", r.stderr)})


def sheets(video: Path, out: Path, duration: float, tile_w: int, per_sheet: int, cols: int):
    """1 thumb/second with the second burned in, tiled into readable sheets."""
    td = out / "_thumbs"
    td.mkdir(parents=True, exist_ok=True)
    vf = (f"fps=1,scale={tile_w}:-1,"
          f"drawtext=fontfile='{FONT}':text='%{{eif\\:n\\:d}}s':x=6:y=6:"
          f"fontsize={max(16, tile_w // 10)}:fontcolor=yellow:box=1:boxcolor=black@0.75:boxborderw=4")
    run(["ffmpeg", "-y", "-i", str(video), "-vf", vf, str(td / "t_%04d.jpg")])
    thumbs = sorted(td.glob("t_*.jpg"))
    sd = out / "sheets"
    sd.mkdir(parents=True, exist_ok=True)
    made = []
    for i in range(0, len(thumbs), per_sheet):
        chunk = thumbs[i:i + per_sheet]
        rows = math.ceil(len(chunk) / cols)
        dst = sd / f"sheet_{i // per_sheet + 1:02d}.jpg"
        r = run(["ffmpeg", "-y", "-start_number", str(i + 1),
                 "-i", str(td / "t_%04d.jpg"), "-frames:v", "1",
                 "-vf", f"tile={cols}x{rows}:padding=6:margin=6:color=black",
                 "-q:v", "3", str(dst)])
        if dst.exists():
            made.append({"file": dst.name, "from_s": i, "to_s": i + len(chunk) - 1})
    return made, len(thumbs)


def hook_frames(video: Path, out: Path, secs: float, fps: float, width: int):
    d = out / "hook"
    d.mkdir(parents=True, exist_ok=True)
    vf = (f"fps={fps},scale={width}:-1,"
          f"drawtext=fontfile='{FONT}':text='%{{eif\\:n/{fps}\\:f\\:2}}s':x=8:y=8:"
          f"fontsize=34:fontcolor=yellow:box=1:boxcolor=black@0.75:boxborderw=6")
    run(["ffmpeg", "-y", "-t", str(secs), "-i", str(video), "-vf", vf,
         "-q:v", "2", str(d / "hook_%02d.jpg")])
    return sorted(p.name for p in d.glob("hook_*.jpg"))


def cut_frames(video: Path, out: Path, cuts: list, width: int, limit: int = 60):
    """A readable frame just after each cut — for reading on-screen text/graphics."""
    d = out / "cuts"
    d.mkdir(parents=True, exist_ok=True)
    made = []
    for t in cuts[:limit]:
        dst = d / f"cut_{t:07.2f}s.jpg".replace(" ", "0")
        run(["ffmpeg", "-y", "-ss", str(t + 0.12), "-i", str(video), "-frames:v", "1",
             "-vf", f"scale={width}:-1", "-q:v", "2", str(dst)])
        if dst.exists():
            made.append(dst.name)
    return made


def transcribe(video: Path, out: Path, model_name: str, lang: str, threads: int = 4) -> dict:
    # cpu_threads must stay low. Higher values make MKL request allocations that
    # fail on this machine ("mkl_malloc: failed to allocate memory"), especially
    # while the system disk is near-full and the pagefile cannot grow.
    from faster_whisper import WhisperModel
    model = WhisperModel(model_name, device="cpu", compute_type="int8", cpu_threads=threads)
    segments, info = model.transcribe(str(video), language=lang, word_timestamps=True,
                                      vad_filter=True, beam_size=5,
                                      condition_on_previous_text=False)
    segs, words, lines = [], [], []
    for s in segments:
        segs.append({"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()})
        lines.append(f"{s.start:6.2f}–{s.end:6.2f}  {s.text.strip()}")
        for w in (s.words or []):
            words.append({"t": round(w.start, 2), "w": w.word.strip()})
    (out / "transcript.txt").write_text("\n".join(lines), encoding="utf-8")
    (out / "transcript_plain.txt").write_text(
        " ".join(s["text"] for s in segs), encoding="utf-8")
    (out / "transcript.json").write_text(
        json.dumps({"segments": segs, "words": words}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    return {"language": info.language, "language_prob": round(info.language_probability, 2),
            "n_segments": len(segs), "n_words": len(words)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--out", default=None)
    ap.add_argument("--model", default="large-v3")
    ap.add_argument("--lang", default="ru")
    ap.add_argument("--threads", type=int, default=4)
    ap.add_argument("--scene", type=float, default=0.25)
    ap.add_argument("--hook-secs", type=float, default=6.0)
    ap.add_argument("--hook-fps", type=float, default=2.0)
    ap.add_argument("--frame-w", type=int, default=560)
    ap.add_argument("--tile-w", type=int, default=260)
    ap.add_argument("--per-sheet", type=int, default=40)
    ap.add_argument("--cols", type=int, default=8)
    ap.add_argument("--frames-only", action="store_true")
    ap.add_argument("--transcribe-only", action="store_true")
    args = ap.parse_args()

    video = Path(args.video).resolve()
    if not video.exists():
        sys.exit(f"video not found: {video}")
    out = Path(args.out).resolve() if args.out else video.parent.parent / "_work" / video.stem
    out.mkdir(parents=True, exist_ok=True)
    aj = out / "analysis.json"
    summary = json.loads(aj.read_text(encoding="utf-8")) if aj.exists() else {}
    summary["video"] = video.name

    if not args.transcribe_only:
        meta = ffprobe_meta(video)
        summary["meta"] = meta
        print(f"[meta] {meta['duration_s']}s · {meta['fps']}fps · "
              f"{meta['width']}x{meta['height']} · vertical={meta['vertical']} · audio={meta['has_audio']}")

        cut_sets = {}
        for th in (0.15, 0.25, 0.40):
            c = scene_cuts(video, th)
            iv = [round(b - a, 2) for a, b in zip(c, c[1:])]
            cut_sets[str(th)] = {
                "count": len(c),
                "avg_interval_s": round(sum(iv) / len(iv), 2) if iv else None,
                "min_interval_s": min(iv) if iv else None,
                "max_interval_s": max(iv) if iv else None,
                "times": c,
            }
            print(f"[cuts@{th}] n={len(c)} avg={cut_sets[str(th)]['avg_interval_s']}s")
        summary["cuts"] = cut_sets
        primary = cut_sets["0.25"]["times"]

        sh, nth = sheets(video, out, meta["duration_s"], args.tile_w, args.per_sheet, args.cols)
        hk = hook_frames(video, out, args.hook_secs, args.hook_fps, args.frame_w)
        cf = cut_frames(video, out, primary, args.frame_w)
        summary["frames"] = {"sheets": sh, "thumbs": nth, "hook": hk, "cut_frames": cf}
        print(f"[frames] sheets={len(sh)} (thumbs={nth}) · hook={len(hk)} · cut_frames={len(cf)}")

    if not args.frames_only:
        if summary.get("meta", {}).get("has_audio", True):
            print(f"[transcribe] {video.name} model={args.model}...")
            try:
                summary["transcript"] = transcribe(video, out, args.model, args.lang, args.threads)
                t = summary["transcript"]
                print(f"[transcribe] {video.name} lang={t['language']}({t['language_prob']}) "
                      f"segments={t['n_segments']} words={t['n_words']}")
            except Exception as e:
                summary["transcript"] = {"error": str(e)}
                print(f"[transcribe] ERROR {video.name}: {e}")
        else:
            summary["transcript"] = {"skipped": "no audio"}

    aj.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[done] {video.name} -> {out}")


if __name__ == "__main__":
    main()
