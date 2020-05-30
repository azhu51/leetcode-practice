# https://leetcode-cn.com/problems/plus-one/

from typing import List

class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    if not digits: return 0


    tmp = str(int(''.join([str(s) for s in digits])) + 1)
    print(tmp)
    ans = []

    for c in tmp:
      ans.append(int(c))

    return ans

s = Solution()
s.plusOne([1,2,3])