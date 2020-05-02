
# https://leetcode-cn.com/problems/unique-paths-ii/



# https://leetcode-cn.com/problems/unique-paths-ii/

class Solution(object):
  def uniquePathsWithObstacles(self, obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    row = len(obstacleGrid)
    col = len(obstacleGrid[0])
    dp = [[0 for i in range(col)] for j in range(row)]

    if obstacleGrid[0][0] == 1:
      return 0

    # initialize the dp array
    for i in range(row):
      if obstacleGrid[i][0] == 1:
        break
      else:
        dp[i][0] = 1

    for i in range(col):
      if obstacleGrid[0][i] == 1:
        break
      else:
        dp[0][i] = 1

    for i in range(1, row):
      for j in range(1, col):
        if obstacleGrid[i][j] == 0:
          dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        else:
          dp[i][j] = 0

    return dp[row - 1][col - 1]

