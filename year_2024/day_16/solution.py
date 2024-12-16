import argparse

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from utils.aoc_utils import *
sys.setrecursionlimit(10000)

# should've done Dijkstra's oh well no aoc timelimit
class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.lines = self.file.splitlines()
        self.mp = list(map(list, self.lines))

    dirs = {
        0: (0, 1),
        1: (0, -1),
        2: (1, 0),
        3: (-1, 0)
    }
    turns = {
        0: [2, 3],
        1: [2, 3],
        2: [0, 1],
        3: [0, 1]
    }
    inverse = {
        0: 1,
        1: 0,
        2: 3,
        3: 2
    }
    def go(self, pos, dir, score):
        if mpget(self.dp, pos)[dir] > score:
            self.dp[pos[0]][pos[1]][dir] = score
            # print(pos, dir, score)
            new_pos = add(pos, self.dirs[dir])
            if 0 <= new_pos[0] < self.n and 0 <= new_pos[1] < self.m and mpget(self.mp, new_pos) != '#':
                self.go(add(pos, self.dirs[dir]), dir, score + 1)
            for other in self.turns[dir]:
                self.go(pos, other, score + 1000)

    def part1(self):
        self.n, self.m = mplen(self.mp)
        print(self.n, self.m)
        start_pos = (0, 0)
        end_pos = (0,0)

        self.dp = []
        for i in range(self.n):
            self.dp.append([])
            for j in range(self.m):
                self.dp[-1].append([1000000000, 1000000000, 1000000000, 1000000000])
                if mpget(self.mp, (i, j)) == 'S':
                    start_pos = (i, j)
                elif mpget(self.mp, (i, j)) == 'E':
                    end_pos = (i, j)

        self.go(start_pos, 0, 0)
        val = min(self.dp[end_pos[0]][end_pos[1]])
        return val

    def check(self, pos, dir, target):
        curr_score = self.dp[pos[0]][pos[1]][dir]
        if curr_score != target:
            return
        self.good.add(pos)
        prev_place = add(pos, self.dirs[self.inverse[dir]])
        self.check(prev_place, dir, curr_score - 1)

        for other_dirs in self.turns[dir]:
            self.check(pos, other_dirs, curr_score - 1000)

    def part2(self):
        self.n, self.m = mplen(self.mp)
        print(self.n, self.m)
        start_pos = (0, 0)
        end_pos = (0,0)

        self.good = set()

        self.dp = []
        for i in range(self.n):
            self.dp.append([])
            for j in range(self.m):
                self.dp[-1].append([1000000000, 1000000000, 1000000000, 1000000000])
                if mpget(self.mp, (i, j)) == 'S':
                    start_pos = (i, j)
                elif mpget(self.mp, (i, j)) == 'E':
                    end_pos = (i, j)

        self.go(start_pos, 0, 0)

        m = min(self.dp[end_pos[0]][end_pos[1]])
        print(m)
        for d in range(4):
            if self.dp[end_pos[0]][end_pos[1]][d] == m:
                self.check(end_pos, d, m)

        return len(self.good)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
