
# https://leetcode-cn.com/contest/biweekly-contest-26/problems/consecutive-characters/

class Solution:
  def maxPower(self, s: str) -> int:

    prev = ""
    max = -1
    res = 0

    for word in s:
      if word != prev:
        res = 1
        if res >= max:
          max = res

      if word == prev:
        res = res + 1
        if res >= max:
          max = res
      prev = word

    return max





s = Solution()
print(s.maxPower(s = "hooraaaaaaaaaaay"))