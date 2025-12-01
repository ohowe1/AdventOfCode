import argparse

import sys
import os
from pkgutil import get_loader

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from utils.aoc_utils import *

class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.codes = self.file.splitlines()

        self.pad1 = [['7', '8', '9'],
                     ['4', '5', '6'],
                     ['1', '2', '3'],
                     [None, '0', 'A']]
        self.pad1_dp = {}
        self.pad2 = [[None, '^', 'A'],
                     ['<', 'v', '>']]
        self.pad2_dp = {}

    def get_locations(self, pad, start, end):
        start_pos = (-1, -1)
        end_pos = (-1, -1)
        for i in range(len(pad)):
            for j in range(len(pad[i])):
                if pad[i][j] == start:
                    start_pos = (i, j)
                if pad[i][j] == end:
                    end_pos = (i, j)
        return start_pos, end_pos

    def pad1_dirs(self, start, end):
        start_pos, end_pos = self.get_locations(self.pad1, start, end)

        ans = []
        if start_pos[1] < end_pos[1]:
            ans += ['>'] * (end_pos[1] - start_pos[1])
        elif start_pos[1] > end_pos[1]:
            ans += ['<'] * (start_pos[1] - end_pos[1])

        if start_pos[0] < end_pos[0]:
            ans += ['v'] * (end_pos[0] - start_pos[0])
        elif start_pos[0] > end_pos[0]:
            ans += ['^'] * (start_pos[0] - end_pos[0])
        return ans

    def pad2_ideal_directions(self, start, end):
        if (start, end) in self.pad2_dp:
            return self.pad2_dp[(start, end)]

        start_pos, end_pos = self.get_locations(self.pad2, start, end)

        # always go right first if need to go right, then go down, then go left, then go down to avoid the None
        ans = []
        while start_pos[1] < end_pos[1]:
            ans.append('>')
            start_pos = add(start_pos, (0, 1))

        while start_pos[0] < end_pos[0]:
            ans.append('v')
            start_pos = add(start_pos, (1, 0))

        while start_pos[1] > end_pos[1]:
            ans.append('<')
            start_pos = add(start_pos, (0, -1))

        while start_pos[0] > end_pos[0]:
            ans.append('^')
            start_pos = add(start_pos, (-1, 0))

        ans.append('A')
        # self.pad2_dp[(start, end)] = ans
        return ans

    def solve_code(self, code):
        robot_1_instructions = self.pad1_dirs('A', code[0])
        for i in range(1, len(code)):
            robot_1_instructions += self.pad1_dirs(code[i - 1], code[i])
        print('!', ''.join(robot_1_instructions))
        # we need to do robot_1_instructions in some order, then click A

        robot_2_instructions = self.pad2_ideal_directions('A', robot_1_instructions[0])
        for i in range(1, len(robot_1_instructions)):
            robot_2_instructions += self.pad2_ideal_directions(robot_1_instructions[i - 1], robot_1_instructions[i])
        print(''.join(robot_2_instructions))

        robot_3_instructions = self.pad2_ideal_directions('A', robot_2_instructions[0])
        for i in range(1, len(robot_2_instructions)):
            robot_3_instructions += self.pad2_ideal_directions(robot_2_instructions[i - 1], robot_2_instructions[i])
        print(''.join(robot_3_instructions))

        return robot_3_instructions


    def part1(self):
        ans = [self.solve_code(code) for code in self.codes]

        comp = 0
        for code, answer in zip(self.codes, ans):
            print(int(code[:len(code) - 1]), len(answer))
            comp += int(code[:-1]) * len(answer)
        return comp

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
