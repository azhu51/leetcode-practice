# https://leetcode-cn.com/problems/generate-parentheses/

from typing import List

# https://leetcode-cn.com/problems/generate-parentheses/solution/ru-men-ji-bie-de-hui-su-fa-xue-hui-tao-lu-miao-don/

class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    cur_str = ""
    res = []


    self.dfs(cur_str, n, n, res)
    return res

  def dfs(self,cur_str, left, right, res):
    if left == 0 and right == 0:
      res.append(cur_str)
      return
    if left > right:
      return
    if left > 0:
      self.dfs(cur_str + '(', left -1, right, res)
    if right > 0:
      self.dfs(cur_str + ')', left, right -1, res)

  def generateParenthesisII(self, n):
    ans = []

    def dfs(path , left, right):
      if len(path) == 2 * n:
        ans.append(''.join(path))
        return
      if left < n:
        path.append('(')
        dfs(path, left + 1, right)
        path.pop()
      if left > right:
        path.append(')')
        dfs(path, left, right + 1)
        path.pop()

    dfs([], 0, 0)
    return ans


