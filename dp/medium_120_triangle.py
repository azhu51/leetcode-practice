# https://leetcode-cn.com/problems/triangle/

# from bottom to top

class Solution(object):
  def minimumTotal(self, triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """

    n = len(triangle)
    for row in range(n-2, -1, -1):
      for col in range(len(triangle[row])):
        triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])
    return triangle[0][0]


s = Solution()
print(s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))