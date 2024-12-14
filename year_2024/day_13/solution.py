import argparse
import math

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def subtract(a, b):
    return a[0] - b[0], a[1] - b[1]

def negate(a):
    return -a[0], -a[1]

def in_range(a, b):
    return 0 <= a[0] <= b[0] and 0 <= a[1] <= b[1]

class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.lines = self.file.split('\n\n')

        self.machines = []
        for line in self.lines:
            lines = line.splitlines()
            button_a = lines[0]

            xA = int(button_a[button_a.index('+') + 1: button_a.index(',')])
            bS = button_a.index('Y')
            yA = int(button_a[button_a.index('+', bS) + 1:])

            button_b = lines[1]
            xB = int(button_b[button_b.index('+') + 1: button_b.index(',')])
            bS = button_b.index('Y')
            yB = int(button_b[button_b.index('+', bS) + 1:])

            prize = lines[2]
            xP = 10000000000000 + int(prize[prize.index('=') + 1: prize.index(',')])
            bS = prize.index('Y')
            yP = 10000000000000 + int(prize[prize.index('=', bS) + 1:])

            self.machines.append(((xA, yA), (xB, yB), (xP, yP)))

    def part1(self):
        tot = 0
        for bA, bB, p in self.machines:
            print(bA, bB, p)
            self.dp = {}
            q = [(0, (0, 0))]
            while len(q)>0:
                t = q[0]
                cost = t[0]
                tp = t[1]
                q.pop(0)

                a_add = add(tp, bA)
                if in_range(a_add, p):
                    if (a_add not in self.dp) or cost + 3 < self.dp[a_add]:
                        self.dp[a_add] = cost + 3
                        q.append((cost + 3, a_add))

                b_add = add(tp, bB)
                if in_range(b_add, p):
                    if (b_add not in self.dp) or cost + 1 < self.dp[b_add]:
                        self.dp[b_add] = cost + 1
                        q.append((cost + 1, b_add))
            if p in self.dp:
                tot += self.dp[p]
        return tot

    def part2(self):
        tot = 0
        for bA, bB, p in self.machines:
            b = (p[0] * bA[1] - p[1] * bA[0]) // (bA[1] * bB[0] - bB[1] * bA[0])
            a = (p[0] * bB[1] - p[1] * bB[0]) // (bB[1] * bA[0] - bB[0] * bA[1])
            print(a, b)

            if bA[0] * a + bB[0] * b == p[0] and bA[1] * a + bB[1] * b == p[1]:
                tot += 3 * a + b
        return tot

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
