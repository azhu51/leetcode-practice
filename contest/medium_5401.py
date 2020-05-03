
#https://leetcode-cn.com/contest/weekly-contest-187/problems/check-if-all-1s-are-at-least-length-k-places-away/

from typing import List


class Solution:
  def kLengthApart(self, nums: List[int], k: int) -> bool:
    if not nums: return False
    if 1 not in nums: return True

    idx = []
    for i in range(0, len(nums)):
      if nums[i] == 1:
        idx.append(i)
    flag = False

    if len(idx) == 1:
      return True

    for i in range(0, len(idx)-1):
      if(idx[i+1] - idx[i]) > k:
        flag = True
      else:
        flag = False

    return flag


s = Solution()
print(s.kLengthApart(nums = [0,0,0], k = 1))