
# https://leetcode-cn.com/contest/weekly-contest-190/problems/max-dot-product-of-two-subsequences/

from typing import List

class Solution:
  def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    m = len(nums2)

    dp = [[0] * n for _ in range(m)]

    for i in range(m):
      for j in range(n):
        if i == 0 and j == 0:
          dp[i][j] = nums2[i] * nums1[j]

        elif i == 0:
          dp[i][j] = max(dp[i][j - 1], nums2[i] * nums1[j])
        elif j == 0:
          dp[i][j] = max(dp[i - 1][j], nums2[i] * nums1[j])
        else:
          dp[i][j] = max(dp[i - 1][j], dp[i][j - 1],
                         dp[i - 1][j - 1] + nums2[i] * nums1[j],
                         nums2[i] * nums1[j])

    return dp[m - 1][n - 1]

