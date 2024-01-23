#!/bin/bash
# source run_all.sh
#
echo #############################################
echo    Press Esc at anytime to skip example
echo #############################################
echo conda install conda-forge::mshr
echo

for f in *.py
    do
        echo "Processing $f script.."
        python3 "$f"
    done

