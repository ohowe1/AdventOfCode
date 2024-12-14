import argparse

class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.lines = [list(a) for a in self.file.splitlines()]

    def add(self, a, b):
        return (a[0] + b[0], a[1] + b[1])
    def process_region(self, point):
        q = [point]
        data = [point]
        target = self.lines[point[0]][point[1]]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.used_area.add(point)
        while len(q) > 0:
            t = q[0]
            q.pop(0)
            for d in directions:
                new_ = self.add(t, d)
                if 0 <= new_[0] < self.n and 0 <= new_[1] < self.m and new_ not in self.used_area and self.lines[new_[0]][new_[1]] == target:
                    q.append(new_)
                    data.append(new_)
                    self.used_area.add(new_)
        self.regions.append(data)
    def thing(self, a, b):
        if b[0] == 0:
            return (a[0] - 1, a[1])
        else:
            return (a[0], a[1] - 1)
    def get_perimiter(self, region):
        total = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        region.sort()
        used_sides = set()
        for r in region:
            for d in directions:
                new_ = self.add(r, d)
                if new_ not in region:
                    other_side = self.thing(new_, d)
                    # print(new_, other_side, r)
                    if (other_side, d) not in used_sides:
                        total += 1
                    used_sides.add((new_, d))
        return total


    def part1(self):
        self.regions = []
        self.used_area = set()
        self.n = len(self.lines)
        self.m = len(self.lines[0])
        for i in range(self.n):
            for j in range(self.m):
                if (i, j) not in self.used_area:
                    self.process_region((i, j))

        print(self.regions)
        total = 0
        i = 0
        for region in self.regions:
            area = len(region)

            perimiter = self.get_perimiter(region)
            if i == 0:
                print('a', area, perimiter)
                i += 1

            total += area * perimiter
        return total


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
