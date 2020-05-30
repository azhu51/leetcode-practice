
# https://leetcode-cn.com/problems/majority-element/
from typing import List

class Solution:
  def majorityElement(self, nums: List[int]) -> int:

    return sorted(nums)[int(len(nums)/2)]
