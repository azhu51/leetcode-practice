
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    if not nums or len(nums) == 1: return len(nums)

    i,j = 0, 1

    while j < len(nums):
      if nums[i] == nums[j]:
        j = j + 1
      else:
        i = i + 1
        nums[i] = nums[j]
        j = j + 1


    return i + 1
