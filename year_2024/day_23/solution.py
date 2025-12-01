import argparse

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from utils.aoc_utils import *


def can_have(comp_bits, subset_bits):
    return subset_bits & ~comp_bits == 0


class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        self.lines = self.file.splitlines()

        self.adj_matrix = {}
        self.with_t = set()
        self.seen = set()
        for line in self.lines:
            c1, c2 = line.split('-')

            if c1.startswith('t'):
                self.with_t.add(c1)
            if c2.startswith('t'):
                self.with_t.add(c2)

            if c1 not in self.adj_matrix:
                self.adj_matrix[c1] = set()
            if c2 not in self.adj_matrix:
                self.adj_matrix[c2] = set()

            self.adj_matrix[c1].add(c2)
            self.adj_matrix[c2].add(c1)

    def get_ordered(self, s1, s2):
        if s1 < s2:
            return s1, s2
        else:
            return s2, s1

    def part1(self):
        sets = set()

        checked = set()
        for comp in self.with_t:
            for c in self.adj_matrix[comp]:
                id = self.get_ordered(comp, c)
                if id in checked:
                    continue
                checked.add(id)

                for c2 in self.adj_matrix[c]:
                    id2 = self.get_ordered(comp, c2)
                    id3 = self.get_ordered(c, c2)
                    if id2 in checked or id3 in checked:
                        continue
                    if c2 in self.adj_matrix[comp]:
                        sets.add((comp, c, c2))

        return len(sets)

    def check_starting_at(self, start):
        # lsp complained with just 1 so added int
        best = (int(1), 1 << self.name_to_id[start])

        self.seen_parents.add(start)
        q = [(start, best)]
        while len(q) > 0:
            curr, data = q.pop(0)
            best = max(best, data)

            cnt, subset = data
            for neighbor in self.adj_matrix[curr]:
                # don't do a search on subsets including parents we've already seen because all those are already searched
                if neighbor in self.seen_parents:
                    continue
                n_i = self.name_to_id[neighbor]
                if can_have(self.masks[n_i], subset):
                    new_subset = subset | (1 << n_i)
                    # checking if this element is already in the subset through equality of them should reduce lookups in set, probably doesn't save much time but why not
                    if new_subset == subset or new_subset in self.seen:
                        continue
                    self.seen.add(new_subset)
                    q.append((neighbor, (cnt + 1, new_subset)))


        return best

    def part2(self):
        self.name_to_id = {}
        self.id_to_name = {}
        i = 0
        for comp in self.adj_matrix:
            self.name_to_id[comp] = i
            self.id_to_name[i] = comp
            i += 1
        self.masks = [0] * len(self.name_to_id)
        for comp, friends in self.adj_matrix.items():
            mask = 0
            for friend in friends:
                mask |= 1 << self.name_to_id[friend]

            self.masks[self.name_to_id[comp]] = mask

        best = (0, 0)
        self.seen_parents = set()
        for comp in self.adj_matrix:
            best = max(best, self.check_starting_at(comp))

        optimal_subset = best[1]
        ans = []
        i = 0
        while optimal_subset > 0:
            if optimal_subset & 0b1 != 0:
                ans.append(i)
            i += 1
            optimal_subset >>= 1


        return ','.join(sorted([self.id_to_name[i] for i in ans]))



if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
