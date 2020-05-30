# https://leetcode-cn.com/problems/valid-palindrome/

class Solution:
  def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    tmp = []
    for c in s:
      if c.isdigit() or c.isalpha():
        tmp.append(c)
    return ''.join(tmp) == ''.join(tmp)[::-1]




s = Solution()
print(s.isPalindrome(s="A man, a plan, a canal: Panama"))