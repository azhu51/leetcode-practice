
# https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/

from typing import List

class Solution:
  def subarraysDivByK(self, A: List[int], K: int) -> int:
    record = {0: 1}
    total, ans = 0, 0
    for elem in A:
      print(record)
      total += elem
      modulus = total % K
      same = record.get(modulus, 0)
      ans += same
      record[modulus] = same + 1


    return ans


s =Solution()
s.subarraysDivByK(A = [4,5,0,-2,-3,1], K = 5)

