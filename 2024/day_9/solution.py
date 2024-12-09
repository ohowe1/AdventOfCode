import argparse

class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.lines = self.file.splitlines()[0]

    def part1(self):
        strin = []
        is_file = True
        i = 0
        for c in self.lines:
            val = str(i)
            if not is_file:
                val = '.'
            else:
                i += 1
            strin += ([val] * int(c))
            is_file = not is_file
        print(strin)
        left = 0
        right = len(strin) - 1
        while left < right:
            if strin[left] != '.':
                left += 1
                continue
            if strin[right] == '.':
                right -= 1
                continue

            print("s'<", left, right)
            strin[left] = strin[right]
            strin[right] = '.'
            left += 1
            right -= 1
        print(''.join(strin))

        t = 0
        for i in range(len(strin)):
            if strin[i] == '.':
                break
            t += i * int(strin[i])
        return t


    def part2(self):
        elms = []
        is_file = True
        i = 0
        for c in self.lines:
            if not is_file:
                elms.append(('.', int(c)))
            else:
                val = str(i)
                i += 1
                elms.append((val, int(c)))
            is_file = not is_file

        print(elms)
        new_elms = []
        moved_already = set()
        j = len(elms) - 1
        while j > 0:
            if elms[j][0] == '.' or elms[j][0] == 'X' or elms[j][0] in moved_already:
                j -= 1
                continue
            moved = False
            for i in range(0, j):
                if elms[i][0] == '.' and elms[j][1] <= elms[i][1]:
                    moved_already.add(elms[j][0])
                    elms[i] = (elms[i][0], elms[i][1] - elms[j][1])
                    elms.insert(i, (elms[j][0], elms[j][1]))
                    moved = True
                    elms[j + 1] = ('.', elms[i][1])
                    break
            if not moved:
                j -= 1

        print(elms)
        final = []
        for val, qty in elms:
            if val == 'X':
                continue
            final += ([val] * int(qty))
        print(''.join(final))

        t = 0
        for i in range(len(final)):
            if final[i] == '.':
                continue
            t += i * int(final[i])
        return t

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
