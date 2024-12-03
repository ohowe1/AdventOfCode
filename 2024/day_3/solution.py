import argparse
import re

# i don't like regex :|
class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.line = self.file

    def part1(self):
        pattern = r"mul\(\d+,\d+\)"
        s = 0
        for r in re.findall(pattern, self.line):
            a = r[4:-1].split(',')
            s += (int(a[0]) * int(a[1]))
        return s

    def part2(self):
        pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
        s = 0
        enable = True
        for r in re.findall(pattern, self.line):
            if r == 'do()':
                enable = True
            elif r == 'don\'t()':
                enable = False
            elif enable:
                a = r[4:-1].split(',')
                s += (int(a[0]) * int(a[1]))
        return s

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
