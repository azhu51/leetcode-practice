# https://leetcode-cn.com/problems/permutations/
from typing import List

class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    import itertools
    ans = []
    for elem in list(itertools.permutations(nums)):
      ans.append(list(elem))

    return ans

  # 回溯
  def permuteII(self, nums:List[int]):
    if not nums: return []

    res = []
    path = []
    used = [False] * len(nums)
    depth = 0
    self.dfs(nums, len(nums), res, depth, path, used)

    return res

  def dfs(self, nums, n, res, depth, path, used):
    if depth == n:
      res.append(list(path))
      return

    for i in range(n):
      if used[i]:
        continue
      path.append(nums[i])
      used[i] = True
      self.dfs(nums, n, res, depth + 1, path, used)
      path.pop()
      used[i] = False


s = Solution()
print(s.permuteII([1,2,3]))
