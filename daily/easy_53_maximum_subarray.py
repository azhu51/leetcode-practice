
#https://leetcode-cn.com/problems/maximum-subarray/

class Solution(object):
  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    pre = 0
    maxAns = nums[0]

    for i in range(0, len(nums)):
      pre = max(pre + nums[i], nums[i])
      maxAns = max(maxAns, pre)

    return maxAns

