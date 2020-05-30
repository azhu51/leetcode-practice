# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/

from typing import List

class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    short = []
    long = []
    if len(nums1) >= len(nums2):
      short = nums2
      long = nums1
    else:
      short = nums1
      long = nums2

    tmp_map = {}

    for i in short:
      if i not in tmp_map:
        tmp_map[i] = 1
      else:
        tmp_map[i] = tmp_map[i] + 1

    ans = []
    for j in long:
      if j in tmp_map and tmp_map[j] > 0:
        ans.append(j)
        tmp_map[j] = tmp_map[j] - 1

    return ans


s = Solution()
s.intersect(nums1=[4,9,5], nums2=[9,4,9,8,4])