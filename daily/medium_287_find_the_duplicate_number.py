from typing import List

class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    import collections
    obj = collections.Counter(nums)

    for key in obj:
      if obj[key] > 1:
        return key

    return 0

s = Solution()
print(s.findDuplicate(nums=[1,3,4,2,2]))
