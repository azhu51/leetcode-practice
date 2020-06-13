
# https://leetcode-cn.com/problems/palindrome-partitioning/

from typing import List

class Solution:
  def partition(self, s: str) -> List[List[str]]:
    s_len = len(s)
    res = []

    if s_len == 0: return res

    stack = []
    self.helper(s, 0, s_len, stack, res)
    return res


  def helper(self, s, start, s_len, path, res):
    if start == s_len:
      res.append(list(path))
      return

    for i in range(start, s_len):
      if not self.checkPalindrome(s[start:i+1]):
        continue

      path.append(s[start:i+1])
      self.helper(s, i+1, s_len, path, res)
      path.pop()



  def checkPalindrome(self, s):
    return s == s[::-1]
