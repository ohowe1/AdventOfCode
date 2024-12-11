import argparse

class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.lines = self.file.splitlines()[0].split()
        self.dp = {}

    def children(self, elm, i):
        if i == 0:
            return 1
        if (elm, i) in self.dp:
            return self.dp[(elm, i)]
        s_elm = str(elm)
        if elm == 0:
            self.dp[(elm, i)] = self.children(1, i - 1)
        elif len(s_elm) % 2 == 0:
            s = self.children(int(s_elm[:len(s_elm) // 2]), i - 1)
            s += self.children(int(s_elm[len(s_elm) // 2:]), i - 1)
            self.dp[(elm, i)] = s
        else:
            s = self.children(elm * 2024, i - 1)
            self.dp[(elm, i)] = s
        return self.dp[(elm, i)]

    def part1(self):
        total = 0
        for elm in self.lines:
            i_elm = int(elm)
            total += self.children(i_elm, 25)
        return total

    def part2(self):
        total = 0
        for elm in self.lines:
            i_elm = int(elm)
            total += self.children(i_elm, 75)
        return total

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', default=0, type=int, help='Part (1/2, 0 for both)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
