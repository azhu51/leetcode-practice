# https://leetcode-cn.com/problems/power-of-three/

class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    if n == 0: return False
    if n == 1: return True

    tmp = float(n)
    while True:
      print(tmp)
      if tmp == 0:
        break
      if len(str(tmp).split('.')[1]) > 1:
        break
      if tmp == 3.0:
        return True
      tmp = tmp / 3

    return False

  def isPowerOfThreeII(self, n):
    while n > 1:
      n = n / 3
    return n == 1

s = Solution()
s.isPowerOfThree(27)