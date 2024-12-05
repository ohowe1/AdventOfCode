import argparse


# this one is very spaget
class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.depend, self.updates = self.file.split('\n\n')
        self.depend = self.depend.splitlines()
        self.updates = [list(map(int, line.split(','))) for line in self.updates.splitlines()]

        self.dmap = {}
        for de in self.depend:
            a, b = map(int, de.split('|'))
            if b not in self.dmap:
                self.dmap[b] = set()
            self.dmap[b].add(a)

    def part1(self):
        t = 0
        for update in self.updates:
            total = set(update)
            seen = set()
            good = True
            for elm in update:
                if elm not in self.dmap:
                    seen.add(elm)
                    continue
                for d in self.dmap[elm]:
                    if d not in seen and d in total:
                        good = False
                        break
                if not good:
                    break
                seen.add(elm)
            if good:
                t += update[len(update) // 2]
        return t


    def part2(self):
        to_process = []
        t = 0
        for update in self.updates:
            total = set(update)
            seen = set()
            good = True
            for elm in update:
                if elm not in self.dmap:
                    seen.add(elm)
                    continue
                for d in self.dmap[elm]:
                    if d not in seen and d in total:
                        good = False
                        break
                if not good:
                    break
                seen.add(elm)
            if not good:
                to_process.append(update)

        for update in to_process:
            local_dependenceis = {}
            total = set(update)
            for elm in update:
                if elm in self.dmap:
                    local_dependenceis[elm] = total & self.dmap[elm]
                else:
                    local_dependenceis[elm] = set()
            final = []
            while len(local_dependenceis) > 0:
                for k in list(local_dependenceis.keys()):
                    if len(local_dependenceis[k]) == 0:
                        del local_dependenceis[k]
                        final.append(k)
                        for k2 in local_dependenceis:
                            local_dependenceis[k2].discard(k)
            t += final[len(final) // 2]
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
