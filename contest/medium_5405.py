
# https://leetcode-cn.com/contest/weekly-contest-188/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

from typing import List

class Solution:

  def comput(self, arr, i, j):
    res = 0
    for p in range(i, j):
      res = res ^ arr[p]
    return res


  def computk(self, arr, j, k):
    res = 0
    for p in range(j, k+1):
      res = res ^ arr[p]
    return res

  def countTriplets(self, arr: List[int]) -> int:
    res = []

    for i in range(0, len(arr)):
      for j in range(i+1,len(arr)):
        for k in range(j, len(arr)):
          if 0 <= i < j<=k<len(arr):
            a = self.comput(arr,i,j)
            b = self.computk(arr,j,k)
            if a == b:
              res.append([i,j,k])

    return len(res)




s = Solution()
print(s.countTriplets(arr = [2,3]))