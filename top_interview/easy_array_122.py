
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:

    if sorted(prices) == prices:
      return max(prices) - min(prices)

    if sorted(prices, reverse=True) == prices:
      return 0



    ans = 0
    for i in range(0, len(prices)-1):
      if prices[i+1] > prices[i]:
        ans += prices[i+1] - prices[i]

    return ans

s = Solution()
#s.maxProfit(prices=[7,1,5,3,6,4])
#print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([6,1,3,2,4,7]))