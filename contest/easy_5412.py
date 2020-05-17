
# https://leetcode-cn.com/contest/weekly-contest-189/problems/number-of-students-doing-homework-at-a-given-time/


from typing import List

class Solution:
  def busyStudent(self, startTime: List[int], endTime: List[int],
                  queryTime: int) -> int:
    res = 0

    for i in range(0, len(startTime)):
      if  startTime[i] <= queryTime <= endTime[i]:
        res = res + 1

    return res


s = Solution()
print(s.busyStudent(startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7))