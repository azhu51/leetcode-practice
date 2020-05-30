
# https://leetcode-cn.com/problems/roman-to-integer/


# 这题懂了就非常简单。首先建立一个HashMap来映射符号和值，然后对字符串从左到右来，
# 如果当前字符代表的值不小于其右边，就加上该值；
# 否则就减去该值。以此类推到最左边的数，最终得到的结果即是答案
# from VictorWei

class Solution:
  def romanToInt(self, s: str) -> int:
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for i in range(len(s)):
      print(ans)
      if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
        print(ans, s[i])
        ans -= a[s[i]]
      else:
        print(ans, s[i])
        ans += a[s[i]]
    return ans


s = Solution()
s.romanToInt(s="MCMXCIV")