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
    val = 0
    for line in self.lines:
        most_sig = 0
        least_sig = 0
        for i in range(len(line)):
            ci = int(line[i])
            if ci > most_sig and i < len(line) - 1:
                most_sig = ci
                least_sig = 0
            else:
                if ci > least_sig:
                    least_sig = ci
        val += int(str(most_sig) + str(least_sig))

    return val
  
  def part2(self):
    count = 0
    for line in self.lines:
      dp = make_2d(0, len(line) + 1, 13)

      for l in range(1, 13):
        for i in range(len(line) - 1, -1, -1):
          if len(line) - i < l:
            continue
          dp[i][l] = max(dp[i + 1][l], int(line[i]) * (10 ** (l - 1)) + dp[i + 1][l - 1])
      count += dp[0][12]
    return count
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
