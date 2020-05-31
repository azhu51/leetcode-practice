
# https://leetcode-cn.com/problems/rotate-array/

from typing import List

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    nums[0:] = nums[len(nums) - k:len(nums)] + nums[0:len(nums) - k]


s = Solution()
s.rotate([1,2,3,4,5,6,7], k = 3)


