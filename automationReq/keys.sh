#!/bin/bash

while read -r name device; do
    python3 createKeys.py $device
done < elements.txt




