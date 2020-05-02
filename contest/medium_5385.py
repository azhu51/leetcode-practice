
# https://leetcode-cn.com/contest/biweekly-contest-25/problems/max-difference-
# you-can-get-from-changing-an-integer/
class Solution:
  def maxDiff(self, num: int):


    res = [-1]

    for x in range(0, 10):
      for y in range(0, 10):

        if str(x) in str(num):
          a = str(num).replace(str(x), str(y))

          if a != 0 and a[0] != "0":
            res.append(int(a))

    return max(res) - min(res)



s = Solution()
print(s.maxDiff(123456))