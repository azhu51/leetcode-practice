
# https://leetcode-cn.com/contest/weekly-contest-191/problems/maximum-product-of-two-elements-in-an-array/

from typing import  List

class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    if not nums: return 0

    max_ = max(nums)
    max_idx = nums.index(max(nums))

    ans = []
    for i in range(0, len(nums)):
      if i!=max_idx:
        ans.append( (max_-1) * (nums[i]-1) )

    return max(ans)



s = Solution()
print(s.maxProduct(nums = [1,5,4,5]))
