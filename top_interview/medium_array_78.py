
# https://leetcode-cn.com/problems/subsets/

# https://leetcode-cn.com/problems/subsets/solution/zi-ji-by-leetcode/


# https://leetcode-cn.com/problems/subsets/solution/hui-su-si-xiang-tuan-mie-pai-lie-zu-he-zi-ji-wen-t/

from typing import List

class Solution:
  # 递归
  def subsets(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    output = [[]]

    for num in nums:
      tmp = []
      for curr in output:
        tmp = tmp + [curr + [num]]
      output = output + tmp
    return output

  # 回溯
  # 幂集是所有长度从 0 到 n 所有子集的组合。
  # 回溯法是一种探索所有潜在可能性找到解决方案的算法。如果当前方案不是正确的解决方案，
  # 或者不是最后一个正确的解决方案，则回溯法通过修改上一步的值继续寻找解决方案。
  def subsetsII(self, nums:List[int]):
    def backtrack(first=0, curr=[]):
      if len(curr) == k:
        output.append(curr[:])

      for i in range(first, n):
        curr.append(nums[i])
        backtrack(i+1, curr)
        curr.pop()

    output = []
    n = len(nums)
    for k in range(n+1):
      backtrack()
    return output

  # bit
  def subsetsIII(self, nums:List[int]):
    n = len(nums)
    output = []

    for i in range(2 ** n, 2**(n+1)):
      bitmask = bin(i)[3:]
      output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

    return output




s = Solution()
print(s.subsetsIII(nums=[1,2,3]))