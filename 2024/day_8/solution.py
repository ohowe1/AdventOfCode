import argparse

def add(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]
def subtract(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1]
class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.lines = self.file.splitlines()

        self.freqs = {}
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                if self.lines[i][j] == '.':
                    continue
                if self.lines[i][j] not in self.freqs:
                    self.freqs[self.lines[i][j]] = []
                self.freqs[self.lines[i][j]].append((i,j))
        for key in self.freqs:
            self.freqs[key].sort()

    def part1(self):
        points = set()
        for key in self.freqs:
            for i in range(len(self.freqs[key])):
                for j in range(i + 1, len(self.freqs[key])):
                    point_1 = self.freqs[key][i]
                    point_2 = self.freqs[key][j]
                    points.add(point_1)
                    points.add(point_2)

                    diff = subtract(point_2, point_1)

                    ab_1 = subtract(point_1, diff)
                    while 0 <= ab_1[0] < len(self.lines) and 0 <= ab_1[1] < len(self.lines[0]):
                        points.add(ab_1)
                        ab_1 = subtract(ab_1, diff)
                    ab_2 = add(point_2, diff)
                    while 0 <= ab_2[0] < len(self.lines) and 0 <= ab_2[1] < len(self.lines[0]):
                        points.add(ab_2)
                        ab_2 = add(ab_2, diff)

        return len(points)

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
