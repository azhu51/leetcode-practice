
# https://leetcode-cn.com/problems/decode-string/

class Solution:
  def decodeString(self, s: str) -> str:
    stk = []
    for ch in s:
      if ch == ']':
        sub = ''
        while stk[-1] != '[':
          sub = stk.pop() + sub
        stk.pop()
        n = ''
        while stk and stk[-1].isdigit():
          n = stk.pop() + n
        stk.append(int(n) * sub)
      else:
        stk.append(ch)

    return ''.join(stk)

s = Solution()
s.decodeString(s="3[a]2[bc]")