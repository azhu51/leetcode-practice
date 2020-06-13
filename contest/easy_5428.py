
# https://leetcode-cn.com/contest/weekly-contest-192/problems/shuffle-the-array/

from typing import List

class Solution:
  def shuffle(self, nums: List[int], n: int) -> List[int]:
    ans = []
    x = []
    y = []
    for i in range(0, n):
      x.append(nums[i])

    for j in range(n, len(nums)):
      y.append(nums[j])


    for p in range(0, n):
      ans.append(x[p])
      ans.append(y[p])


    return ans

s = Solution()
print(s.shuffle([2,5,1,3,4,7], n = 3))



