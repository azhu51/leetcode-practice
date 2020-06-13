
# https://leetcode-cn.com/problems/new-21-game/

class Solution:
  # def new21Game(self, N: int, K: int, W: int) -> float:
  #   if K == 0:
  #     return 1.0
  #   dp = [0.0] * (K + W)
  #   for i in range(K, min(N,K + W - 1) + 1):
  #     dp[i] = 1.0
  #   for i in range(K -1, -1, -1):
  #     for j in range(1, W + 1):
  #       dp[i] += dp[i + j]/ W
  #   return dp[0]
  def new21Game(self, N: int, K: int, W: int) -> float:
    dp = [0.0] * (K + W)
    for k in range(K, min(N + 1, K + W)):
      dp[k] = 1.0

    S = min(N - K + 1, W)
    for k in range(K -1, -1,-1):
      dp[k] = S / float(W)
      S += dp[k] - dp[k + W]

    return dp[0]

