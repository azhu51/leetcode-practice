# https://leetcode-cn.com/problems/sum-of-two-integers/

class Solution:
  def getSumII(self, a: int, b: int) -> int:
    return sum([a,b])

  def getSum(self, a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    # 2^32
    MASK = 0x100000000
    # 整型最大值
    MAX_INT = 0x7FFFFFFF
    MIN_INT = MAX_INT + 1
    while b != 0:
      # 计算进位
      carry = (a & b) << 1
      # 取余范围限制在 [0, 2^32-1] 范围内
      a = (a ^ b) % MASK
      b = carry % MASK
    return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

#https://leetcode-cn.com/problems/sum-of-two-integers/solution/wei-yun-suan-xiang-jie-yi-ji-zai-python-zhong-xu-y/
# https://leetcode-cn.com/problems/sum-of-two-integers/solution/0msfu-xian-ji-suan-ji-zui-ji-ben-de-jia-fa-cao-zuo/