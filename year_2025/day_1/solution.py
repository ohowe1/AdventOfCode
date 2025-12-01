import argparse

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
    self.lines = self.file.splitlines()
    
  def part1(self):
    position = 50
    count = 0
    for line in self.lines:
      mult = -1 if line[0] == 'L' else 1

      adding = mult * int(line[1:])
      
      position += adding
      position += 100
      position %= 100
      
      if position == 0:
        count += 1
    return count
  
  def part2(self):
    position = 50
    count = 0
    for line in self.lines:
      mult = -1 if line[0] == 'L' else 1

      adding = int(line[1:])

      trivial_passes = adding // 100
      adding_mod = (adding % 100) * mult

      if position + adding_mod >= 100 or (position + adding_mod <= 0 and position > 0):
        trivial_passes += 1

      position += adding_mod
      position += 100
      position %= 100
      print(position)
      
      count += trivial_passes
      
      
    return count

  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()