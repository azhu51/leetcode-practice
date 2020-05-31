
# https://leetcode-cn.com/problems/factorial-trailing-zeroes/

class Solution:
  def trailingZeroes(self, n: int) -> int:
    if n < 5: return 0

    res = 0

    while n>=5:
      res += n//5
      n /= 5
    return res


s = Solution()
print(s.trailingZeroes(7))