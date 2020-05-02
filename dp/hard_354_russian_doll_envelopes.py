# https://leetcode-cn.com/problems/russian-doll-envelopes/

class Solution(object):
  def maxEnvelopes(self, envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    envelopes.sort(key=lambda x: (x[0], -x[1]))

    def lengthOfLIS(nums):
      if not nums:
        return 0
      dp = []
      for i in range(len(nums)):
        dp.append(1)
        for j in range(i):
          if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)
      return max(dp)

    return lengthOfLIS([i[1] for i in envelopes])
