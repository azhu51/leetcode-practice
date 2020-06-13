
# https://leetcode-cn.com/problems/game-of-life/

from typing import List
# https://leetcode-cn.com/problems/game-of-life/solution/sheng-ming-you-xi-by-leetcode-solution/
class Solution:
  def gameOfLife(self, board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    rows = len(board)
    cols = len(board[0])

    neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1),
                 (1, 1)]

    copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

    for row in range(rows):
      for col in range(cols):

        live_neighbors = 0
        for neighbor in neighbors:

          r = (row + neighbor[0])
          c = (col + neighbor[1])

          # check live cell
          if (r < rows and r >=0) and (c<cols and c >=0) and (copy_board[r][c] == 1):
            live_neighbors += 1


        # rule 1 or 3
        if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
          board[row][col] = 0

        if copy_board[row][col] == 0 and live_neighbors == 3:
          board[row][col] = 1




s = Solution()
s.gameOfLife(
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
)