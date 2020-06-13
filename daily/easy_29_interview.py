
# https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/

from typing import List

class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
      return list()

    rows, columns = len(matrix), len(matrix[0])

    order = list()

    left, right = 0, columns - 1
    top, bottom = 0, rows - 1

    while left<= right and top<=bottom:
      for col in range(left, right + 1):
        order.append(matrix[top][col])
      for row in range(top + 1, bottom + 1):
        order.append(matrix[row][right])
      if left < right and top < bottom:
        for col in range(right - 1, left, -1):
          order.append(matrix[bottom][col])
        for row in range(bottom, top, -1):
          order.append(matrix[row][top])

      left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

    return order


s = Solution()
s.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])