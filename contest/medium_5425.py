
# https://leetcode-cn.com/contest/weekly-contest-191/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

from typing import List

class Solution:

  def findMaxGap(self, l):
    max_gap = 0

    for i in range(1,len(l)):
      if l[i] - l[i-1] > max_gap:
        max_gap = l[i] - l[i-1]

    return max_gap

  def maxArea(self, h: int, w: int, horizontalCuts: List[int],
              verticalCuts: List[int]) -> int:

    h_list = [0]
    v_list = [0]

    sorted_h = sorted(horizontalCuts)
    sorted_v = sorted(verticalCuts)

    for i in range(0, len(sorted_h)):
      h_list.append(sorted_h[i])
    h_list.append(h)

    for j in range(0, len(sorted_v)):
      v_list.append(sorted_v[j])
    v_list.append(w)


    max_gap_h = self.findMaxGap(h_list)
    max_gap_v = self.findMaxGap(v_list)

    return (max_gap_v * max_gap_h) % (10 ** 9 + 7)



s = Solution()
#print(s.maxArea(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]))
#print(s.maxArea(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]))
print(s.maxArea(h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]))