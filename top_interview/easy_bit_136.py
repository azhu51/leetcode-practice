
# https://leetcode-cn.com/problems/single-number/

from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:

    # 交换律：a ^ b ^ c <= > a ^ c ^ b
    #
    # 任何数于0异或为任何数
    # 0 ^ n = > n
    #
    # 相同的数异或为0: n ^ n = > 0

    # var
    # a = [2, 3, 2, 4, 4]
    #
    # 2 ^ 3 ^ 2 ^ 4 ^ 4
    # 等价于
    # 2 ^ 2 ^ 4 ^ 4 ^ 3 = > 0 ^ 0 ^ 3 = > 3

    if not nums: return
    a = 0
    for i in range(0, len(nums)):
      a = a ^ nums[i]
    return a
