import argparse

class Solution:
  filename_real_input = 'real.in'
  filename_test_input = 'test.in'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()
    self.levels = []
    for line in self.lines:
        ints = list(map(int, line.split()))
        self.levels += [ints]
    print(self.levels)
    
  def part1(self):
    tot = 0
    for level in self.levels:
        good = True
        increasing = level[1] > level[0]
        last = level[0]
        if increasing:
            last -= 1
        else:
            last += 1
        for i in level:
            if (increasing and (i - last > 0 and i - last <= 3)) or ((not increasing) and (last - i > 0 and last - i <= 3)):
                pass
            else:
                good = False
                break
            last = i
        if good:
            tot += 1
    return tot
  
  def part2(self):
    tot = 0
    for le in self.levels:
        ggood = False
        for i in range(len(le)):
            level = le[:i] + le[i + 1:]
            good = True
            increasing = level[1] > level[0]
            last = level[0]
            if increasing:
                last -= 1
            else:
                last += 1
            for i in level:
                if (increasing and (i - last > 0 and i - last <= 3)) or ((not increasing) and (last - i > 0 and last - i <= 3)):
                    pass
                else:
                    good = False
                    break
                last = i
            if good:
                ggood = True
                break
        if ggood:
            tot += 1
    return tot
            
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
