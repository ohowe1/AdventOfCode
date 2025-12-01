import argparse

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from utils.aoc_utils import *

class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def make_lock(self, lines):
        lock = []

        for i in range(len(lines[0])):
            val = 0
            while val + 1 < len(lines) and lines[val + 1][i] == '#':
                val += 1
            lock.append(val)
        return lock
    
    def make_key(self, lines):
        key = []

        for i in range(len(lines[0])):
            val = 0
            while val + 1 < len(lines) and lines[val + 1][i] == '.':
                val += 1
            key.append(5 - val)
        return key


    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        elements = self.file.split('\n\n')

        self.keys = []
        self.locks = []
        for element in elements:
            element = element.splitlines()
            if element[0] == '#####':
                self.locks.append(self.make_lock(element))
            else:
                self.keys.append(self.make_key(element))

        print(self.keys, self.locks)
    def part1(self):
        cnt = 0
        for kI in range(len(self.keys)):
            for lI in range(len(self.locks)):
                works = all([k + l <= 5 for k, l in zip(self.keys[kI], self.locks[lI])])
                if works:
                    cnt += 1
        return cnt



    def part2(self):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
