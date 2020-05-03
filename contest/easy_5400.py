
# https://leetcode-cn.com/contest/weekly-contest-187/problems/destination-city/

from typing import List

class Solution:
  def destCity(self, paths: List[List[str]]) -> str:
    if not paths: return ""
    if len(paths) == 1: return paths[0][1]

    start_city = set()
    end_city = set()
    for i in range(0, len(paths)):
      start_city.add(paths[i][0])
      end_city.add(paths[i][1])

    return "".join(end_city - start_city)


s = Solution()
print(s.destCity(paths=[["B","C"],["D","B"],["C","A"]]))
