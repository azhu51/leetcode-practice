
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    if not prices: return 0

    max_ans = 0
    min_ = prices[0]
    for i in range(0, len(prices)):
      max_ans = max(max_ans, prices[i] - min_)
      min_ = min(min_, prices[i])

    return max_ans
