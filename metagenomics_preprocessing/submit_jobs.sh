#!/bin/bash

read -p "Enter patient response (lowercase): " response

python make_qsub.py response

for f in *pbs
do
    qsub $f
done
