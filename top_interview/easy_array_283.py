
# https://leetcode-cn.com/problems/move-zeroes/

from typing import List

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    raw_len = len(nums)
    while 0 in nums:
      nums.remove(0)
    filter_len = len(nums)
    for i in range(raw_len - filter_len):
      nums.append(0)


s = Solution()
print(s.moveZeroes(nums=[0,1,0,3,12]))