
# https://leetcode-cn.com/problems/longest-increasing-subsequence/

class Solution(object):
  def lengthOfLIS(self, nums):
    if not nums:
      return 0

    dp = []

    for i in range(len(nums)):
      dp.append(1)
      for j in range(i):
        if nums[i] > nums[j]:
          dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

