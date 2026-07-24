#!/usr/bin/env bash
# Sequential transcription: one fresh Python process per video.
#
# A single long-lived process accumulates allocator pressure and dies with
# "mkl_malloc: failed to allocate memory" partway through the corpus. A fresh
# process per video starts clean. Loading large-v3 also needs ~600 MB of free
# disk headroom, so we bail out early rather than thrash a full volume.
set -u
cd "$(dirname "$0")/.."

MIN_FREE_MB=${MIN_FREE_MB:-1200}
ok=0; fail=0; skip=0

for f in referens-reels-hook/raw/*.mp4; do
  stem=$(basename "$f" .mp4)
  if [ -f "referens-reels-hook/_work/$stem/transcript.json" ]; then
    echo "[skip] $stem (already done)"; skip=$((skip+1)); continue
  fi
  free=$(df -m /c | tail -1 | awk '{print $4}')
  if [ "$free" -lt "$MIN_FREE_MB" ]; then
    echo "[STOP] only ${free}MB free (need ${MIN_FREE_MB}MB) — aborting"; break
  fi
  echo "[run ] $stem (${free}MB free)"
  if timeout 900 python tools/ingest.py "$f" --transcribe-only 2>&1 | grep -E "^\[transcribe\]|ERROR"; then :; fi
  if [ -f "referens-reels-hook/_work/$stem/transcript.json" ]; then
    ok=$((ok+1))
  else
    fail=$((fail+1)); echo "[FAIL] $stem"
  fi
done

echo "=== ok=$ok fail=$fail skip=$skip ==="
echo "total transcripts: $(ls referens-reels-hook/_work/*/transcript.json 2>/dev/null | wc -l)/15"
