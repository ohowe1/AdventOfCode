import argparse

import sys
import os

from numpy.f2py.cfuncs import get_needs

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from utils.aoc_utils import *

class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.lines = list(map(int, self.file.splitlines()))

    def get_next_secret(self, num):
        num ^= num * 64
        num %= 16777216
        num ^= num // 32
        num %= 16777216
        num ^= num * 2048
        num %= 16777216

        return num

    def part1(self):
        ans = 0
        for n in self.lines:
            for i in range(2000):
                n = self.get_next_secret(n)
            print(n)
            ans += n
        return ans

    def part2(self):
        diffs = []
        prices = []
        for n in self.lines:
            diff = []
            price = []
            for i in range(2000):
                last_p = n % 10
                n = self.get_next_secret(n)
                diff.append((n % 10) - last_p)
                price.append(n % 10)
            diffs += [diff]
            prices += [price]
        all_four_seqs = {}
        for diff, price in zip(diffs, prices):
            this_seq = set()
            for i in range(len(diff) - 3):
                sub_seq = tuple(diff[i:i+4])
                if sub_seq in this_seq:
                    continue
                if sub_seq in all_four_seqs:
                    all_four_seqs[sub_seq] += price[i + 3]
                else:
                    all_four_seqs[sub_seq] = price[i + 3]
                this_seq.add(sub_seq)
        mx_count = 0
        for diff, count in all_four_seqs.items():
            if count > mx_count:
                print(diff)
                mx_count = count
        return mx_count

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
