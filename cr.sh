#!/bin/bash

# Check if an argument was passed
if [ -z "$1" ]; then
    echo "Usage: $0 <source_file_without_extension>"
    exit 1
fi

# Extract the base name from the argument (e.g., kattis/balanceddiet -> balanceddiet)
BASENAME=$(basename "$1")

# Compile the C++ file using g++-14
g++-14 -x c++ -g -O2 -std=gnu++20 -o "build/$BASENAME" "$1"

# Check if the compilation was successful
if [ $? -eq 0 ]; then
    # Run the compiled program with input redirection
    time "./build/$BASENAME" < input.in
else
    echo "Compilation failed."
    exit 1
fi

