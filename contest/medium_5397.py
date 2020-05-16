# https://leetcode-cn.com/contest/biweekly-contest-26/problems/simplified-fractions/
from typing import List

class Solution:

  def hcf(self, x,y):
    if x > y: smaller = y
    else: smaller = x

    for i in range(1, smaller + 1):
      if ((x % i == 0) and (y % i == 0)):
        hcf = i

    return hcf

  def simplifiedFractions(self, n: int) -> List[str]:
    if n == 0 or n ==1: return []
    res = []
    for i in range(2,n+1):
      for j in range(1, i):
        if self.hcf(i,j) == 1:
          res.append(str(j) + "/" + str(i))

    return res


s = Solution()
print(s.simplifiedFractions(2))