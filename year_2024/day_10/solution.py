import argparse

class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.lines = list(map(list, self.file.splitlines()))
        nl = []
        for line in self.lines:
            nl.append(list(map(int, line)))
        self.lines = nl
        self.n = len(self.lines)
        self.m = len(self.lines[0])
        self.dp = []

    def add(self, t1, t2):
        return (t1[0] + t2[0], t1[1] + t2[1])
    def process(self, start):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = [start]
        v = set()
        v.add(start)
        reached = []
        while len(q) > 0:
            t = q[0]
            q.pop(0)
            for d in dirs:
                new_a = self.add(t, d)
                if (0 <= new_a[0] < self.n) and (0 <= new_a[1] < self.m) and (self.lines[t[0]][t[1]] - 1 == self.lines[new_a[0]][new_a[1]]):
                    reached.append(new_a)
                    v.add(new_a)
                    q.append(new_a)
                    self.dp[new_a[0]][new_a[1]] += 1

    def part1(self):
        self.dp = []
        for i in range(self.n):
            self.dp.append([])
            for j in range(self.m):
                self.dp[i].append(0)
        print(self.dp)

        starts = []
        c = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.lines[i][j] == 9:
                    c += 1
                    self.process((i, j))
                elif self.lines[i][j] == 0:
                    starts.append((i, j))
        print(c)
        t = 0
        for start in starts:
            t += self.dp[start[0]][start[1]]
        return t

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
