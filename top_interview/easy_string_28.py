
# https://leetcode-cn.com/problems/implement-strstr/

class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    if not needle: return 0
    return haystack.find(needle)

  def strStrII(self, haystack: str, needle: str) -> int:
    L, n = len(needle), len(haystack)

    for start in range(n - L + 1):
      if haystack[start: start + L] == needle:
        return start
    return -1


# https://leetcode-cn.com/problems/implement-strstr/solution/kmp-suan-fa-xiang-jie-by-labuladong/
# KMP
