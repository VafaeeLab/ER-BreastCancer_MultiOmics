#!/bin/bash

read -p "Enter input file directory: " response
read -p "Enter output filename: " output

conda activate metaphlan3

merge_metaphlan_tables.py response/* > merged_table.txt

awk '!($2="")' merged_table.txt > merged_table_filtered.txt

awk '{ for(i=1;i<=NF;i++){if(i==NF){printf("%s\n",$NF);}else {printf("%s\t",$i)}}}' merged_table_filtered.txt > output.txt