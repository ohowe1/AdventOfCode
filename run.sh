#!/bin/bash
# script for daily collect content of problem of AOC
# inputs are : DAY, YEAR, PART, [TEST] (TEST is optional)

if [ "$#" -lt 3 ] || [ "$#" -gt 4 ]; then
  echo "Need three or four input arguments in the following order: submit <day> <year> <part> [test]"
  exit 1
fi

DAY=$1
YEAR=$2
PART=$3
TEST=$4

cd ${YEAR}/day_${DAY}

if [ -z "$TEST" ]; then
  python solution.py -part $PART
else
  python solution.py -part $PART -test $TEST
fi