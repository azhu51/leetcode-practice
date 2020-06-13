#https://leetcode-cn.com/problems/product-of-array-except-self/

from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    if not nums: return []
    n = len(nums)
    L,R = [0 for _ in range(n)], [0 for _ in range(n)]
    L[0] = 1
    R[n-1] = 1

    for i in range(0, n-1):
      L[i+1] = L[i] * nums[i]

    for j in range(n-1-1,-1,-1):
      R[j] = R[j+1] * nums[j+1]

    ans = []

    for i in range(n):
      ans.append(L[i]*R[i])

    return ans

  
s = Solution()
s.productExceptSelf([1,2,3,4])




