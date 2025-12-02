import argparse

from bisect import bisect_left, bisect_right
import math
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from utils.aoc_utils import *

class Solution:
  filename_real_input = 'real_input.in'
  filename_test_input = 'test_input.in'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall(r'[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.lines = self.file

    elements = self.lines.split(',')

    self.ranges = list(map(lambda a : list(map(int, a.split('-'))), elements))

  def part1(self):
    total = 0
    for range_ in self.ranges:
      lower_bound = math.floor(range_[0] / (10 ** math.ceil(math.ceil(math.log10(range_[0])) / 2)))
      upper_bound = math.ceil(range_[1] / (10 ** math.ceil(math.floor(math.log10(range_[1])) / 2)))

      for i in range(lower_bound, upper_bound + 1, 1):
        val = int(str(i) * 2)
        if range_[0] <= val <= range_[1]:
          total += val
    return total
          
  
  def part2(self):
    total = 0
    max_upper = 0
    for range_ in self.ranges:
      if range_[1] > max_upper:
        max_upper = range_[1]
    max_upper_digits = math.ceil(math.log10(max_upper))

    vals = set()

    upper_bound = math.ceil(max_upper / (10 ** math.ceil(math.ceil(math.log10(max_upper)) / 2)))
    for i in range(1, upper_bound + 1):
      if i in vals:
        continue

      as_str = str(i)
      for times in range(2, max_upper_digits):
        new_str = int(as_str * times)
        if new_str > max_upper:
          break
        vals.add(new_str)

    
    as_list = list(vals)
    as_list.sort()
    for range_ in self.ranges:
      left = bisect_left(as_list, range_[0])
      for i in range(left, len(as_list)):
        if as_list[i] > range_[1]:
          break
        total += as_list[i]

    return total
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()