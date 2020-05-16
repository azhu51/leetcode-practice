
# https://leetcode-cn.com/contest/weekly-contest-188/problems/build-an-array-with-stack-operations/

from typing import List

class Solution:
  def buildArray(self, target: List[int], n: int) -> List[str]:
    if not target: return []
    res = []
    tmp = []
    for i in range(1, n+1):
      if i in target:
        res.append("Push")
        tmp.append(i)
      if i not in target:
        res.append("Push")
        res.append("Pop")
      if tmp == target:
        break
    return res


s = Solution()
print(s.buildArray(target = [2,3,4], n = 4))
