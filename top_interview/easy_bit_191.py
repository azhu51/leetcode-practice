
# https://leetcode-cn.com/problems/number-of-1-bits/submissions/

class Solution:
  def hammingWeight(self, n: int) -> int:
    return bin(n).count('1')
