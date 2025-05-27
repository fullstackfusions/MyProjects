#!/usr/bin/env bash
shopt -s nullglob nocaseglob

for heic in *.heic; do
  # derive the output filename
  jpg="${heic%.*}.jpg"
  echo "Converting '$heic' → '$jpg'…"
  sips -s format jpeg "$heic" --out "$jpg"
done

echo "Done!"

# Grant permission to execute the script
# chmod +x convert_heic_to_jpg.sh
# Usage: ./convert_heic_to_jpg.sh
