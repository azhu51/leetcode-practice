# https://leetcode-cn.com/problems/maximum-subarray/

from typing import List

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:

    sub_sum = 0
    max_sum = nums[0]

    for i in range(0, len(nums)):
      sub_sum = max(sub_sum + nums[i], nums[i])
      max_sum = max(sub_sum, max_sum)


    return max_sum
