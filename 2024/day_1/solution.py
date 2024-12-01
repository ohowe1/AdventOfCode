import argparse
from collections import Counter

class Solution:
  filename_real_input = 'real.in'
  filename_test_input = 'test.in'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()
    
    self.a = []
    self.b = []
    for line in self.lines:
      a_i, b_i = map(int, line.split())
      self.a += [a_i]
      self.b += [b_i]
    self.b_counter = Counter(self.b)
    self.a.sort()
    self.b.sort()
    
  def part1(self):
    ans = 0
    for a, b in zip(self.a, self.b):
      ans += abs(a - b)
    return ans
  
  def part2(self):
    ans = 0
    for a in self.a:
      ans += a * self.b_counter[a]
    return ans
      
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', default='f', type=str, help='Test mode (t/af)')
  args = parser.parse_args()
  test = True if args.test.lower() in ['true', '1', 't'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part {args.part} ({'test' if test else 'real'}):\n{result}')