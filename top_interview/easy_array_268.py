
# https://leetcode-cn.com/problems/missing-number/
from typing import List

class Solution:
  def missingNumber(self, nums: List[int]) -> int:

    sum_n = 0.5 * len(nums) * (len(nums)+1)
    sum_arr = sum(nums)
    return int(sum_n-sum_arr)

s = Solution()
print(s.missingNumber([3,0,1]))



# 由于异或运算（XOR）满足结合律，并且对一个数进行两次完全相同的异或运算会得到原来的数，因此我们可以通过异或运算找到缺失的数字。
#
# missing
# ​
# =4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)
# =(4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2
# =0∧0∧0∧0∧2
# =2
# ​

