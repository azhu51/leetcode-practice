
# https://leetcode-cn.com/contest/biweekly-contest-25/problems/check-if-a-string-can-break-another-string/

class Solution:

  def checkBreak(self, sub1, sub2):
    n = len(sub1)
    check_set = set()
    for i in range(0, n):
      if sub1[i] == sub2[i]:
        continue
      if sub1[i] > sub2[i]:
        check_set.add(True)
      else:
        check_set.add(False)
    return len(check_set) == 1

  def perm(self, s=''):
    if len(s) <= 1:
      return [s]
    sl = []
    for i in range(len(s)):
      for j in self.perm(s[0:i] + s[i + 1:]):
        sl.append(s[i] + j)
    return sl


  def checkIfCanBreak(self, s1: str, s2: str) -> bool:
    if len(s1) != len(s2): return False


    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))

    if self.checkBreak(s1, s2) == True:
      return True

    return False


    # sub_s1_list = self.perm(s1)
    # sub_s2_list = self.perm(s2)
    #
    #
    # for i in range(0, len(sub_s1_list)):
    #   for j in range(0, len(sub_s2_list)):
    #     if self.checkBreak(sub_s1_list[i], sub_s2_list[j]) == True:
    #       return True
    #
    # return False


s = Solution()
print(s.checkIfCanBreak("leetcodee", "interview"))