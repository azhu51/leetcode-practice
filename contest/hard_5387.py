
#https://leetcode-cn.com/contest/biweekly-contest-25/problems/number-of-ways-to-wear-different-hats-to-each-other/

from typing import List

class Solution:
  def numberWays(self, hats: List[List[int]]) -> int:
    if not hats: return 0

    num = len(hats)




s = Solution()
# print(s.numberWays(hats=[[3,4],[4,5],[5]]))

res = set([])
res.add([1,2,3,4])

print(res)