
# https://leetcode-cn.com/problems/reverse-integer/

class Solution:
  def reverse(self, x: int) -> int:
    if x<10 and x> -10: return x
    tag=""
    if x<= -10: tag,x = "-",-x

    tmp = list(str(x))[::-1]

    if tag=="":
      x = int(''.join([i for i in tmp]))
    else:
      x = 0-int(''.join([i for i in tmp]))

    if -2 ** 31 < x < 2 ** 31 - 1:
      return x
    return 0


s = Solution()
# print(s.reverse(1230))
# print(s.reverse(120))
# print(s.reverse(-123))
s.reverse(901000)



# https://leetcode-cn.com/problems/reverse-integer/solution/tu-jie-7-zheng-shu-fan-zhuan-by-wang_ni_ma/
# x % 10: get last number
# then x / 10