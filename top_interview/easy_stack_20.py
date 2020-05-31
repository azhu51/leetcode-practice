#https://leetcode-cn.com/problems/valid-parentheses/

class Solution:
  def isValid(self, s: str) -> bool:
    if not s: return True
    if len(s) % 2 == 1: return False

    s = list(s)
    tmp_1 = []

    flag = False

    for elem in s:
      if elem=="(" or elem=="[" or elem=="{":
        tmp_1.append(elem)
      if (elem==")" and len(tmp_1)== 0) or (elem=="]" and len(tmp_1)== 0) or (elem=="}" and len(tmp_1)== 0):
        flag = False
        break
      if (elem==")" and tmp_1.pop()!="(") or (elem=="]" and tmp_1.pop()!="[") or (elem=="}" and tmp_1.pop()!="{"):
        flag = False
        break
      flag = True

    if flag and len(tmp_1) > 0:
      flag = False
    return flag

  def isValidII(self, s: str) -> bool:
    dic = {')': '(', ']': '[', '}': '{'}
    stack = []
    for i in s:
      if stack and i in dic:
        if stack[-1] == dic[i]:
          stack.pop()
        else:
          return False
      else:
        stack.append(i)

    return not stack




s = Solution()
print(s.isValid(s="{[]}"))