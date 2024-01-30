#!/bin/bash

# Check if a filename is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <filename>"
  exit 1
fi

filename="$1"
output_file="${filename%.*}_singleline.fasta"

# Check if the input file exists
if [ ! -f "$filename" ]; then
  echo "File '$filename' not found."
  exit 1
fi

# Convert multi-line FASTA to single-line FASTA using awk
awk '/^>/ {printf("%s%s\n",(NR==1)?"":"\n",$0);next} {printf("%s",$0)} END {printf("\n")}' "$filename" > "$output_file"

echo "Conversion completed. Result saved in '$output_file'."
