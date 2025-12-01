import argparse

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from utils.aoc_utils import *

class Gate:
    inputs = []
    operator = None
    output = None

    unsolved_dependendenies = 2

    def __init__(self, in1, in2, operator, out):
        self.inputs = [in1, in2]
        self.inputs.sort()
        self.operator = operator
        self.output = out

    def eval(self, in1, in2):
        if self.operator == 'AND':
            return in1 and in2
        elif self.operator == 'OR':
            return in1 or in2
        else:
            return in1 ^ in2

    def __str__(self):
        return f'{self.inputs[0]} {self.operator} {self.inputs[1]} -> {self.output}'
class Solution:
    filename_real_input = 'real.in'
    filename_test_input = 'test.in'

    def __init__(self, test=False):
        self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
        initial, gates = self.file.split('\n\n')

        self.gates = []
        self.unsolved = []
        self.dependents = {}
        i = 0
        for ln in gates.splitlines():
            in1, op, in2, _, out = ln.split()

            self.gates.append(Gate(in1, in2, op, out))
            if in1 not in self.dependents:
                self.dependents[in1] = []
            if in2 not in self.dependents:
                self.dependents[in2] = []

            self.dependents[in1].append(i)
            self.dependents[in2].append(i)
            i += 1

        self.initial_values = {}
        for ln in initial.splitlines():
            wire, val = ln.split(': ')

            self.initial_values[wire] = val == '1'


    def part1(self):
        can_be_evaluated = []
        values = self.initial_values.copy()

        for wire in self.initial_values:
            if wire not in self.dependents:
                continue

            for dependent in self.dependents[wire]:
                self.gates[dependent].unsolved_dependendenies -= 1

                if self.gates[dependent].unsolved_dependendenies == 0:
                    can_be_evaluated.append(dependent)

        while len(can_be_evaluated) > 0:
            to_eval = can_be_evaluated.pop()
            gate = self.gates[to_eval]

            value = gate.eval(values[gate.inputs[0]], values[gate.inputs[1]])

            values[gate.output] = value
            print(gate.output)
            if gate.output not in self.dependents:
                continue

            for dependent in self.dependents[gate.output]:
                self.gates[dependent].unsolved_dependendenies -= 1

                if self.gates[dependent].unsolved_dependendenies == 0:
                    print('can do', dependent)
                    can_be_evaluated.append(dependent)


        print(values)
        answer = 0
        i = 0
        while True:
            name = f"z{i:02d}"
            if name not in values:
                break

            if values[name]:
                answer |= 1 << i
            i += 1
        return answer


    def part2(self):
        for gate in self.gates:
            if gate.output[0] == 'z' and gate.output != 'z45' and gate.operator != 'XOR':
                print('Non XOR!', gate)
            


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Solution file')
    parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
    parser.add_argument('-test', default='f', type=str, help='Test mode (t/f)')
    args = parser.parse_args()
    test = True if args.test.lower() in ['true', '1', 't'] else False
    solution = Solution(test=test)
    result = solution.part1() if args.part == 1 else solution.part2()
    print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')
