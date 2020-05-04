
# https://leetcode-cn.com/problems/jump-game-ii/

from typing import List

class Solution:
  def jump(self, nums: List[int]) -> int:
    ans , start, end = 0, 0, 1
    while end < len(nums):
      maxPos = 0
      for i in range(start, end):
        maxPos = max(maxPos, i + nums[i])
      start = end
      end = maxPos + 1
      ans += 1
    return ans

  