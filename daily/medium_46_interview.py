
# https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/

class Solution:
  def translateNum(self, num: int) -> int:

    snum = str(num)

    dp = [0 for _ in range(len(snum)+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(snum)+1):
      st = snum[i-2] + snum[i-1]

      if st >= "10" and st <= "25":
        dp[i] = dp[i-1] + dp[i-2]
      else:
        dp[i] = dp[i-1]

    return dp[len(snum)]


s = Solution()
s.translateNum(122)

