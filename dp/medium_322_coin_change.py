
# https://leetcode-cn.com/problems/coin-change/

from typing import List

# 背包问题
# 完全背包问题  物品数量无限个
# 01背包  每种物品要么有要么没有，用一个
# 多重背包  物品数量有限
# 背包问题 n*m 时间复杂度

class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
      for x in range(coin, amount + 1):
        dp[x] = min(dp[x], dp[x-coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1



