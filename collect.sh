#!/bin/bash
# script for daily collect content of problem of AOC
# inputs are : DAY, YEAR (need to respect the order)

if [ "$#" -ne 2 ]; then
  echo "Need two input arguments in the following order: collect <day> <year>"
  exit 1
fi

DAY=$1
YEAR=$2
python scripts/collect.py -d $DAY -y $YEAR