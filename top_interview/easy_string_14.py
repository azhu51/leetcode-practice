# https://leetcode-cn.com/problems/longest-common-prefix/

from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs: return ''

    ans = ""

    len_list = [len(s) for s in strs]
    min_len_str = strs[len_list.index(min(len_list))]

    strs.remove(min_len_str)

    for i in range(len(min_len_str),0,-1):
      key = min_len_str[0:i]
      count = 0

      for elem in strs:
        if elem.startswith(key):
          count = count + 1
        else:
          break

      if count == len(strs):
        ans = key
        break


    return ans

  def longestCommonPrefixII(self, strs):
    if not strs: return ""
    ss = list(map(set, zip(*strs)))
    res = ""
    for i, x in enumerate(ss):
      x = list(x)
      if len(x) > 1:
        break
      res = res + x[0]
    return res




s = Solution()
s.longestCommonPrefix(["flower","flow","flight"])
s.longestCommonPrefix(["dog","racecar","car"])