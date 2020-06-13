
# https://leetcode-cn.com/contest/weekly-contest-192/problems/the-k-strongest-values-in-an-array/

from typing import List

class Solution:
  def getStrongest(self, arr: List[int], k: int) -> List[int]:
    ans = []
    if not arr: return []
    m = self.getM(arr)

    tmp = [[abs(arr[i] - m),arr[i]] for i in range(0,len(arr))]

    sorted_tmp = sorted(tmp,reverse=True)[0:k]
    for i,j in sorted_tmp:
      ans.append(j)

    return ans

  def getM(self, arr):
    sorted_arr = sorted(arr)
    n = len(arr)
    return sorted_arr[int((n-1)/2)]




s = Solution()
s.getStrongest(arr = [6,7,11,7,6,8], k = 5)
