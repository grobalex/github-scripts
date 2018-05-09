#!/bin/bash

for file in *.pdf; do
  if [[ -f "$file" ]]; then
     filename=$(echo "$file" | awk -F'[-]' '{print $2}')
     echo "team-"$filename"-spring18"
     mv "$file" "team-"$filename"-spring18"
  fi
done
