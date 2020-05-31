
# https://leetcode-cn.com/contest/biweekly-contest-27/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
import itertools as it


class Solution:
  def hasAllCodes(self, s: str, k: int) -> bool:
    import itertools as it
    k_all = list(it.product(range(2), repeat=k))
    for elem in k_all:
      if ''.join(str(i) for i in list(elem)) not in s:
        return False

    return True

  def hasAllCodesII(self, s: str, k: int) -> bool:
    this = set(s[i:i + k] for i in range(len(s) - k + 1))
    return len(this) == 2 ** k


s = Solution()
print(s.hasAllCodes(s = "0000000001011100", k = 20))