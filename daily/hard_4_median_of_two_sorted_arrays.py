
from typing import List

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

    merge = []

    for i in range(0, len(nums1)):
      merge.append(nums1[i])

    for j in range(0, len(nums2)):
      merge.append(nums2[j])

    sorted_merge = sorted(merge)


    if len(sorted_merge) % 2 == 0:
      return (sorted_merge[int(len(sorted_merge)/2) - 1] + sorted_merge[int(len(sorted_merge)/2)])/2*1.0

    if len(sorted_merge) % 2 != 0:
      return (sorted_merge[int(len(sorted_merge)/2)]) * 1.0


s = Solution()
print(s.findMedianSortedArrays(nums1=[1,3], nums2=[2,4]))


