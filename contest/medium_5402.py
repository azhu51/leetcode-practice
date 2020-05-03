
# https://leetcode-cn.com/contest/weekly-contest-187/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

from typing import List


class Solution:
  def longestSubarray(self, nums: List[int], limit: int) -> int:
    # if not nums: return 0
    # n = len(nums)
    # res = [0]
    #
    # for i in range(n, 0, -1):
    #   for j in range(0, i):
    #     if len(nums[j:i]) <= max(res):
    #       break
    #     if abs(max(nums[j:i]) - min(nums[j:i])) <= limit:
    #       res.append(len(nums[j:i]))

    if max(nums) == min(nums):
      return len(nums)

    left, right = 0, 0
    length = 1
    while right < len(nums):
      max_ = max(nums[left:right+1])
      min_ = min(nums[left:right+1])
      if max_ - min_ <= limit:
        length = max(length, right - left + 1)
        right += 1
      while max_ - min_ > limit:
        left += 1
        right += 1
        max_ = max(nums[left:right+1])
        min_ = min(nums[left:right+1])
    return length

s = Solution()
print(s.longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0))