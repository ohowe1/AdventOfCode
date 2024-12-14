import argparse
import re


def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def subtract(a, b):
    return a[0] - b[0], a[1] - b[1]

def mult(a, scal):
    return a[0] * scal, a[1] * scal

def negate(a):
    return -a[0], -a[1]


class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.lines = self.file.splitlines()
        self.robots = []

        for line in self.lines:
            nums = re.findall(r'-?\d+', line)

            self.robots.append(((int(nums[0]), int(nums[1])), (int(nums[2]), int(nums[3]))))

    def part1(self):
        w = 11
        h = 7
        w = 101
        h = 103
        poses = []
        for i_pos, v in self.robots:
            new_pos = add(i_pos, mult(v, 100))
            new_pos = (new_pos[0] % w, new_pos[1] % h)
            poses.append(new_pos)

        q1 = sum([1 for pose in poses if pose[0] < w // 2 and pose[1] < h // 2])
        q2 = sum([1 for pose in poses if pose[0] < w // 2 and pose[1] > h // 2])
        q3 = sum([1 for pose in poses if pose[0] > w // 2 and pose[1] < h // 2])
        q4 = sum([1 for pose in poses if pose[0] > w // 2 and pose[1] > h // 2])
        return q1 * q2 * q3 * q4

    def part2(self):
        # i didn't like this
        w = 11
        h = 7
        w = 101
        h = 103
        poses = []
        a = 1
        while True:
            new_robots = []
            s = set()
            for i_pos, v in self.robots:
                new_pos = add(i_pos, mult(v, 1))
                new_pos = (new_pos[0] % w, new_pos[1] % h)
                new_robots.append((new_pos, v))
                s.add(new_pos)
            if len(s) == len(self.robots):
                return a
            self.robots = new_robots
            a += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
