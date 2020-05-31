
# https://leetcode-cn.com/contest/weekly-contest-191/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

from typing import List

class Solution:
  def minReorder(self, n: int, connections: List[List[int]]) -> int:
    flag = False

    # every city can go to 0
    for elem in connections:
      if elem[1] == 0:
        flag = True
      if elem[1] != 0:
        flag = False
        break

    if flag:
      return 0

    sorted_con = sorted(connections)

    can_reach_city = set()
    ans = 0
    tmp_con = []
    for start, end  in sorted_con:
      if end == 0:
        can_reach_city.add(start)
        continue
      if start == 0:
        can_reach_city.add(end)
        ans = ans + 1
        continue
      tmp_con.append([start,end])

    for start, end in sorted(tmp_con):
      if end in can_reach_city:
        can_reach_city.add(start)
        continue
      if start in can_reach_city:
        can_reach_city.add(end)
        ans = ans + 1
        continue

    return ans


s = Solution()
print(s.minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]))

