

# https://leetcode-cn.com/contest/biweekly-contest-26/problems/form-largest-integer-with-digits-that-add-up-to-target/

class Solution:
  def largestNumber(self, cost: List[int], target: int) -> str:
    f = [-1 for i in range(target + 1)]
    f[0] = 0
    for i in range(1, target + 1):
      for j in range(len(cost)):
        if i >= cost[j] and f[i - cost[j]] >= 0:
          f[i] = max(f[i], f[i - cost[j]] * 10 + j + 1)
    return str(max(f[target], 0))