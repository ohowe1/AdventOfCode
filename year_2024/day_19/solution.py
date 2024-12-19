import argparse

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from utils.aoc_utils import *

class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.lines = self.file.split('\n\n')

        self.towels = self.lines[0].split(', ')
        self.patterns = self.lines[1].splitlines()

    def can_solve(self, pattern, towels):
        if len(pattern) == 0:
            return True
        if (pattern, towels) in self.dp:
            return self.dp[(pattern, towels)]
        with_towel = False
        for i in range(len(towels)):
            if pattern.startswith(towels[i]):
                with_towel |= self.can_solve(pattern[len(towels[i]):], towels)
                if with_towel:
                    break
        self.dp[(pattern, towels)] = with_towel
        return with_towel

    def amount_solve(self, pattern, towels):
        if len(pattern) == 0:
            return 1
        if (pattern, towels) in self.dp:
            return self.dp[(pattern, towels)]
        with_towel = False
        for i in range(len(towels)):
            if pattern.startswith(towels[i]):
                with_towel += self.can_solve(pattern[len(towels[i]):], towels)
        self.dp[(pattern, towels)] = with_towel
        return with_towel


    def part1(self):
        c = 0
        for pattern in self.patterns:
            self.dp = {}
            if self.can_solve(pattern, tuple(self.towels)):
                c += 1
        return c

    def part2(self):
        c = 0
        for pattern in self.patterns:
            self.dp = {}
            c += self.amount_solve(pattern, tuple(self.towels))
        return c

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
