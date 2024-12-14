import argparse

class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.lines = self.file.splitlines()

    # valid = ["XMAS", "SAMX"]
    valid = ["MAS", "SAM"]
    def check_forward(self, i, j) :
        if j + 4 > len(self.lines[i]):
            return False
        return self.lines[i][j:j+4] in self.valid

    def check_down(self, i, j):
        if i == 6 and j == 9:
            print('!!')
        if i + 4 > len(self.lines):
            return False
        s = ''.join([self.lines[i + d][j] for d in range(4)])
        if i == 6 and j == 9:
            print('!!')
            print(s)
        return s in self.valid

    def check_diag(self, i, j):
        if i + 3 > len(self.lines) or j + 3 > len(self.lines[i]):
            return False
        s = ''.join([self.lines[i + d][j + d] for d in range(3)])
        if i == 0 and j == 1:
            print('!!')
            print(s)
        return s in self.valid

    def check_diag2(self, i, j):
        if i + 3 > len(self.lines) or j < 2:
            return False
        s = ''.join([self.lines[i + d][j - d] for d in range(3)])
        return s in self.valid

    def part1(self):
        c = 0

        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                if self.check_forward(i, j):
                    print(i, j, "f")
                    c += 1
                if self.check_diag(i, j):
                    print(i, j, "d")
                    c += 1
                if self.check_diag2(i, j):
                    print(i, j, "d2")
                    c += 1
                if self.check_down(i, j):
                    print(i, j, "do")
                    c += 1

        return c

    def part2(self):
        diag1 = []
        diag2 = []
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                if self.check_diag(i, j):
                    diag1.append((i, j))
                if self.check_diag2(i, j):
                    diag2.append((i,j))
        pair_set = set()
        for d in diag1:
            added = False
            for d2 in diag2:
                if d[0] == d2[0] and d2[1] - d[1] == 2:
                    if added:
                        print("DF", d, d2)
                        print('pre', len(pair_set))
                    val = (min(d[0], d2[0]) + 1, min(d[1], d2[1]) + 1)
                    pair_set.add(val[0] * len(self.lines) + val[1])
                    if added:
                        print('post', len(pair_set))
                    added = True
        print(pair_set)
        return len(pair_set)



if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
