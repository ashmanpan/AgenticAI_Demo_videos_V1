#!/bin/bash
set -e
cd /home/kpanse/wsl-myprojects/MWC-story

echo "Step 1: Boost incident v3 audio +10dB, convert to stereo..."
ffmpeg -y -i "Incident-management-v1.0-with-narration-v3.mp4" \
  -c:v libx264 -preset fast -crf 23 -r 30 \
  -af "volume=10dB" \
  -c:a aac -b:a 128k -ar 44100 -ac 2 \
  "incident_v3_loud.mp4"
echo "Done. Size: $(ls -lh incident_v3_loud.mp4 | awk '{print $5}')"

echo ""
echo "Step 2: Check volumes..."
echo "Jio intro:"
ffmpeg -i "jio_intro_27s.mp4" -af volumedetect -vn -f null /dev/null 2>&1 | grep mean_volume || true
echo "Incident boosted:"
ffmpeg -i "incident_v3_loud.mp4" -af volumedetect -vn -f null /dev/null 2>&1 | grep mean_volume || true

echo ""
echo "Step 3: Normalize Jio intro to match..."
ffmpeg -y -i "jio_intro_27s.mp4" \
  -c:v copy \
  -af "volume=2dB" \
  -c:a aac -b:a 128k -ar 44100 -ac 2 \
  "jio_intro_matched.mp4"

echo ""
echo "Step 4: Concatenate..."
printf "file 'jio_intro_matched.mp4'\nfile 'incident_v3_loud.mp4'\n" > concat_v3.txt
ffmpeg -y -f concat -safe 0 -i concat_v3.txt -c copy "Incident-management-v3.0-FINAL.mp4"

echo ""
echo "DONE!"
ls -lh "Incident-management-v3.0-FINAL.mp4"
ffprobe -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "Incident-management-v3.0-FINAL.mp4"
