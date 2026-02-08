#!/bin/bash
set -e
cd /home/kpanse/wsl-myprojects/MWC-story

echo "=== Step 1: Extract Jio intro (0-27s) scaled to 1920x996 ==="
ffmpeg -y -i "Cisco Jio OTAP 4.47 V5.3.mp4" \
  -t 27 \
  -vf "scale=1920:996:force_original_aspect_ratio=decrease,pad=1920:996:(ow-iw)/2:(oh-ih)/2:black" \
  -af "volume=2dB" \
  -c:v libx264 -preset fast -crf 23 -r 30 \
  -c:a aac -b:a 128k -ar 44100 -ac 2 \
  part1_jio_intro.mp4
echo "Part 1 done: $(du -h part1_jio_intro.mp4 | cut -f1)"

echo ""
echo "=== Step 2: Boost incident demo narration +15dB, convert to stereo ==="
ffmpeg -y -i "Incident-management-v1.0-with-narration-v3.mp4" \
  -af "volume=15dB" \
  -c:v libx264 -preset fast -crf 23 -r 30 \
  -c:a aac -b:a 128k -ar 44100 -ac 2 \
  part2_demo_loud.mp4
echo "Part 2 done: $(du -h part2_demo_loud.mp4 | cut -f1)"

echo ""
echo "=== Step 3: Extract Cisco ending (280-287s) scaled to 1920x996 ==="
ffmpeg -y -ss 280 -i "Cisco Jio OTAP 4.47 V5.3.mp4" \
  -t 7 \
  -vf "scale=1920:996:force_original_aspect_ratio=decrease,pad=1920:996:(ow-iw)/2:(oh-ih)/2:black" \
  -af "volume=2dB" \
  -c:v libx264 -preset fast -crf 23 -r 30 \
  -c:a aac -b:a 128k -ar 44100 -ac 2 \
  part3_cisco_ending.mp4
echo "Part 3 done: $(du -h part3_cisco_ending.mp4 | cut -f1)"

echo ""
echo "=== Step 4: Check volumes ==="
echo -n "Part 1 (Jio intro): "
ffmpeg -i part1_jio_intro.mp4 -af volumedetect -vn -f null /dev/null 2>&1 | grep mean_volume | awk '{print $5, $6}'
echo -n "Part 2 (Demo):      "
ffmpeg -i part2_demo_loud.mp4 -af volumedetect -vn -f null /dev/null 2>&1 | grep mean_volume | awk '{print $5, $6}'
echo -n "Part 3 (Ending):    "
ffmpeg -i part3_cisco_ending.mp4 -af volumedetect -vn -f null /dev/null 2>&1 | grep mean_volume | awk '{print $5, $6}'

echo ""
echo "=== Step 5: Concatenate all 3 parts ==="
printf "file 'part1_jio_intro.mp4'\nfile 'part2_demo_loud.mp4'\nfile 'part3_cisco_ending.mp4'\n" > concat_v4.txt
ffmpeg -y -f concat -safe 0 -i concat_v4.txt -c copy "Incident-management-v4.0-FINAL.mp4"

echo ""
echo "=== DONE ==="
ls -lh "Incident-management-v4.0-FINAL.mp4"
echo -n "Duration: "
ffprobe -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "Incident-management-v4.0-FINAL.mp4"
