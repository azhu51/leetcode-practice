# https://leetcode-cn.com/problems/rotate-image/

from typing import List

class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """


    matrix[:] = map(list, zip(*matrix[::-1]))


  def rotateII(self, matrix):
    n = len(matrix[0])
    for i in range(n):
      for j in range(i,n):
        matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


    for i in range(n):
      matrix[i].reverse()


s = Solution()
s.rotate(matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
])