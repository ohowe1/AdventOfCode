import argparse

class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.lines = self.file.splitlines()

    def part1(self):
        c = 0
        for line in self.lines:
            target, elements = line.split(':')
            target = int(target)
            elements = list(map(int, elements.split()))

            possibles = set()
            possibles.add(elements[0])
            for i in range(1, len(elements) - 1):
                to_add = set()
                for possible in possibles:
                    if possible * elements[i] <= target:
                        to_add.add(possible * elements[i])
                    if possible + elements[i] <= target:
                        to_add.add(possible + elements[i])
                possibles = to_add

            for possible in possibles:
                if possible * elements[-1] == target or possible + elements[-1] == target:
                    c += target
                    break
        return c

    def part2(self):
        c = 0
        for line in self.lines:
            target, elements = line.split(':')
            target = int(target)
            elements = list(map(int, elements.split()))

            possibles = set()
            possibles.add(elements[0])
            for i in range(1, len(elements) - 1):
                to_add = set()
                for possible in possibles:
                    if possible * elements[i] <= target:
                        to_add.add(possible * elements[i])
                    if possible + elements[i] <= target:
                        to_add.add(possible + elements[i])
                    if int(str(possible) + str(elements[i])) <= target:
                        to_add.add(int(str(possible) + str(elements[i])))
                possibles = to_add

            for possible in possibles:
                if possible * elements[-1] == target or possible + elements[-1] == target or int(str(possible) + str(elements[-1])) == target:
                    c += target
                    break
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
