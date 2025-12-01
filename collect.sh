#!/bin/bash
PARAMS=$(cat day.txt)

python3 main.py collect $PARAMS $@
