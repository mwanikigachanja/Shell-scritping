#!/bin/bash

# Set your name
name="yourName"

# Find the highest number file that already exists
max_file=$(ls -1 | grep "${name}" | awk -F"${name}" '{print $2}' | sort -n | tail -n1)
if [ -z "$max_file" ]; then
  max_file=0
fi

# Create the next 25 files with increasing numbers
for i in $(seq 1 25); do
  next_file=$((max_file+i))
  touch "${name}${next_file}"
done


#Execute: ./useradd
