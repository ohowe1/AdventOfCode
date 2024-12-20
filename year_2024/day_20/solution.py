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
        self.mp = make_2d(True, len(self.lines), len(self.lines[0]))
        self.n, self.m = mplen(self.mp)
        self.start_pos = (0, 0)
        self.end_pos = (0, 0)
        for i in range(self.n):
            for j in range(self.m):
                if self.lines[i][j] == '#': self.mp[i][j] = False
                if self.lines[i][j] == 'S':
                    self.start_pos = (i, j)
                elif self.lines[i][j] == 'E':
                    self.end_pos = (i, j)

    def dfs_from_point(self, pos):
        q = [pos]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        seen.add(pos)
        dist = make_2d(1000000000, self.n, self.m)

        dist[pos[0]][pos[1]] = 0
        while len(q) > 0:
            p = q.pop(0)
            for d in dirs:
                n = add(d, p)
                if n not in seen and mpin(self.mp, n) and self.mp[n[0]][n[1]]:
                    seen.add(n)
                    dist[n[0]][n[1]] = dist[p[0]][p[1]] + 1
                    q.append(n)
        return dist, seen

    def part1(self):
        end_dist, _ = self.dfs_from_point(self.end_pos)
        start_dist, seen = self.dfs_from_point(self.start_pos)

        to_beat = mpget(end_dist, self.start_pos)

        cnt = 0
        jmps = [(2, 0), (-2, 0), (0, 2), (0, -2), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for p in seen:
            for j in jmps:
                p2 = add(p, j)
                if not mpin(self.mp, p2) or not mpget(self.mp, p2):
                    continue
                if mpget(start_dist, p) + mpget(end_dist, p2) + abs(p[0] - p2[0]) + abs(p[1] - p2[1]) + 100 <= to_beat:
                    cnt += 1

        return cnt


    def part2(self):
        end_dist, _ = self.dfs_from_point(self.end_pos)
        start_dist, seen = self.dfs_from_point(self.start_pos)

        to_beat = mpget(end_dist, self.start_pos)

        cnt = 0
        for p in seen:
            for i in range(-20, 21):
                for j in range(-(20 - abs(i)), 21 - abs(i)):
                    if i == 0 and j == 0: continue
                    p2 = (p[0] + i, p[1] + j)
                    if not mpin(self.mp, p2) or not mpget(self.mp, p2):
                        continue
                    if mpget(start_dist, p) + mpget(end_dist, p2) + abs(p[0] - p2[0]) + abs(p[1] - p2[1]) + 100 <= to_beat:
                        cnt += 1
        return cnt

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
