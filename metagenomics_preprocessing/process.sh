#!/bin/bash

read -p "Comparison of interest: " comparison

find $PWD/comparison -type f -name "*.txt" | while read txt; do
  python3 all_abundance.py $txt --out ../out/comparison/
done