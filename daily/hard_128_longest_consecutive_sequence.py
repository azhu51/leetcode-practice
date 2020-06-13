
# https://leetcode-cn.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    if not nums: return 0

    l = set()
    for i in range(len(nums)):
      l.add(nums[i])


    sorted_nums = sorted(list(l))
    res = []
    tmp = []
    for i in range(0, len(sorted_nums)-1):
      tmp.append(sorted_nums[i+1] - sorted_nums[i])

    count = 0
    for j in range(0, len(tmp)):
      if tmp[j] == 1:
        count = count + 1

      if tmp[j] != 1:
        res.append(count)
        count = 0

    res.append(count)

    return max(res)+1

  def longestConsecutiveII(self, nums):
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
      if num - 1 not in num_set:
        current_num = num
        current_streak = 1

        while current_num + 1 in num_set:
          current_num += 1
          current_streak += 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak




s = Solution()
#print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
#s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6])
s.longestConsecutive([1,2,0,1])
