import argparse

class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.lines = list(map(list, self.file.splitlines()))
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                if self.lines[i][j] == '^':
                    self.start_pos = (i, j)

    def part1(self, extra = None):
        orr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        curr_position = self.start_pos
        curr_orintation = 0
        n = len(self.lines)
        m = len(self.lines[0])

        path = set()
        visited = set()
        path.add(curr_position)
        visited.add((curr_position, curr_orintation))
        while True:
            new = (curr_position[0] + orr[curr_orintation][0], curr_position[1] + orr[curr_orintation][1])
            if 0 <= new[0] < n and 0 <= new[1] < m:
                if self.lines[new[0]][new[1]] == '#' or new == extra:
                    curr_orintation += 1
                    curr_orintation %= 4
                    continue
                else:
                    if (new, curr_orintation) in visited:
                        print((new, curr_orintation))
                        return True
                    visited.add((new, curr_orintation))
                    path.add(new)
                    curr_position = new
            else:
                break
        return (path, len(path))

    def part2(self):
        originalPath, _ = self.part1()

        c = 0
        for p in originalPath:
            if p != self.start_pos and self.part1(p) == True:
                print(p)
                c += 1
        return c

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
