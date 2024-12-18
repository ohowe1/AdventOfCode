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

        self.reg_a = get_ints(self.lines[0])[0]
        self.reg_b = get_ints(self.lines[1])[0]
        self.reg_c = get_ints(self.lines[2])[0]

        self.program = get_ints(self.lines[4])
        print(self.program)

    def part1(self):
        in_pointer = 0

        out = []
        while in_pointer < len(self.program):
            op_code = self.program[in_pointer]
            operand = self.program[in_pointer + 1]

            combo = operand
            if operand == 4:
                combo = self.reg_a
            elif operand == 5:
                combo = self.reg_b
            elif operand == 6:
                combo = self.reg_c

            if op_code == 0:
                num = self.reg_a

                self.reg_a = num // (2 ** combo)
            elif op_code == 1:
                self.reg_b = self.reg_b ^ operand
            elif op_code == 2:
                self.reg_b = combo % 8
            elif op_code == 3:
                if self.reg_a != 0:
                    in_pointer = operand
                    continue
            elif op_code == 4:
                self.reg_b = self.reg_b ^ self.reg_c
            elif op_code == 5:
                out.append(combo % 8)
            elif op_code == 6:
                num = self.reg_a

                self.reg_b = num // (2 ** combo)
            elif op_code == 7:
                num = self.reg_a

                self.reg_c = num // (2 ** combo)
            in_pointer += 2
        return out

    def part2(self):
        self.reg_b = get_ints(self.lines[1])[0]
        self.reg_c = get_ints(self.lines[2])[0]

        prog_i = 0
        prev = [0]
        valid_prev_reg_a = []
        while prog_i < 16:
            for start in prev:
                for i in range(9):
                    self.reg_a = start * (2 ** 3) + i
                    self.reg_b = get_ints(self.lines[1])[0]
                    self.reg_c = get_ints(self.lines[2])[0]
                    p1 = self.part1()
                    if p1 == self.program[-len(p1):]:
                        valid_prev_reg_a.append(start * (2 ** 3) + i)
            prev = valid_prev_reg_a
            valid_prev_reg_a = []
            prog_i += 1
        return min(prev)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
