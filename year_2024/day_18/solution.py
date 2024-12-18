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
        self.lines = self.file.splitlines()

    def has_root(self):
        n, m = 71, 71
        q = [((0, 0), 1)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        while len(q) > 0:
            a, b = q[0]
            q.pop(0)

            for d in dirs:
                new_ = add(a, d)
                if mpin(self.grid, new_) and not mpget(self.grid, new_) and new_ not in visited:
                    if new_ == (n - 1, m - 1):
                        return True
                    q.append((new_, b+1))
                    visited.add(new_)
        return False

    def part1(self):
        n, m = 71, 71
        self.grid = make_2d(False, n, m)

        for i in range(1024):
            a = get_ints(self.lines[i])
            self.grid[a[0]][a[1]] = True

        q = [((0, 0), 1)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        while len(q) > 0:
            a, b = q[0]
            q.pop(0)

            for d in dirs:
                new_ = add(a, d)
                if mpin(self.grid, new_) and not mpget(self.grid, new_) and new_ not in visited:
                    if new_ == (n - 1, m - 1):
                        return b
                    q.append((new_, b+1))
                    visited.add(new_)

    # a little slow but it does the trick
    def part2(self):
        n, m = 71, 71
        self.grid = [[False] * n for i in range(m)]

        for i in range(len(self.lines)):
            a = get_ints(self.lines[i])
            self.grid[a[0]][a[1]] = True
            if not self.has_root():
                return a

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
