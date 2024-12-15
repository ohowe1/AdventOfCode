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
        self.mp = list(map(list, self.lines[0].splitlines()))
        self.instr = ''.join(self.lines[1].splitlines())

    def try_move(self, dir, loc):
        if self.mp[loc[0]][loc[1]] == '#':
            return False
        elif self.mp[loc[0]][loc[1]] == '.':
            return True
        else:
            new_new_loc = add(dir, loc)
            if self.try_move(dir, new_new_loc):
                self.mp[new_new_loc[0]][new_new_loc[1]] = self.mp[loc[0]][loc[1]]
                return True
            return False
    def part1(self):
        robot_loc = (0, 0)
        n = len(self.mp)
        m = len(self.mp[0])
        for i in range(n):
            for j in range(m):
                if self.mp[i][j] == '@':
                    robot_loc = (i, j)
                    # self.mp[i][j] = '.'
                    break

        d = {
            '^': (-1, 0),
            '>': (0, 1),
            '<': (0, -1),
            'v': (1, 0),
        }
        for inst in self.instr:
            dir = d[inst]
            if self.try_move(dir, robot_loc):
                self.mp[robot_loc[0]][robot_loc[1]] = '.'
                robot_loc = add(dir, robot_loc)

        tot = 0
        for i in range(n):
            for j in range(m):
                if self.mp[i][j] == 'O':
                    tot += i * 100 + j
        return tot

    def try_move2(self, dir, loc, dp, bud = False):
        if loc in dp:
            return dp[loc]
        if self.mp[loc[0]][loc[1]] == '#':
            return False
        elif self.mp[loc[0]][loc[1]] == '.':
            return True
        elif self.mp[loc[0]][loc[1]] == '@':
            new_new_loc = add(dir, loc)
            if self.try_move2(dir, new_new_loc, dp):
                # self.mp[new_new_loc[0]][new_new_loc[1]] = self.mp[loc[0]][loc[1]]
                return True
            return False
        else:
            new_new_loc = add(dir, loc)
            can_move_buddy = True
            if dir[0] != 0 and not bud:
                bud_loc = add((0, 1) if self.mp[loc[0]][loc[1]] == '[' else (0, -1), loc)
                can_move_buddy = self.try_move2(dir, bud_loc, dp, True)
            if not can_move_buddy:
                return False
            if self.try_move2(dir, new_new_loc, dp):
                dp[loc] = True
                return True
            dp[loc] = False
            return False
    def move(self, dir, loc, done):
        if loc in done:
            return
        if self.mp[loc[0]][loc[1]] == '#':
            return
        elif self.mp[loc[0]][loc[1]] == '.':
            return
        elif self.mp[loc[0]][loc[1]] == '@':
            new_loc = add(dir, loc)
            done.add(loc)
            self.move(dir, new_loc, done)
            self.mp[new_loc[0]][new_loc[1]] = '@'
            self.mp[loc[0]][loc[1]] = '.'
        else:
            bud_loc = add((0, 1) if self.mp[loc[0]][loc[1]] == '[' else (0, -1), loc)
            new_loc = add(dir, loc)
            done.add(loc)
            self.move(dir, bud_loc, done)
            self.move(dir, new_loc, done)
            self.mp[new_loc[0]][new_loc[1]] = self.mp[loc[0]][loc[1]]
            self.mp[loc[0]][loc[1]] = '.'

    def printmp(self):
        print('\n'.join(map(''.join,self.mp)))
    def part2(self):
        self.mp = list(map(list, self.lines[0].replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.').splitlines()))
        self.printmp()
        robot_loc = (0, 0)
        n = len(self.mp)
        m = len(self.mp[0])
        for i in range(n):
            for j in range(m):
                if self.mp[i][j] == '@':
                    robot_loc = (i, j)
                    break

        d = {
            '^': (-1, 0),
            '>': (0, 1),
            '<': (0, -1),
            'v': (1, 0),
        }
        for inst in self.instr:
            dir = d[inst]
            dp_here = {}
            if self.try_move2(dir, robot_loc, dp_here):
                done = set()
                self.move(dir, robot_loc, done)
                robot_loc = add(dir, robot_loc)

        self.printmp()
        tot = 0
        for i in range(n):
            for j in range(m):
                if self.mp[i][j] == '[':
                    tot += i * 100 + j
        return tot

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
