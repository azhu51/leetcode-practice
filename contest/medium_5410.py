
#https://leetcode-cn.com/contest/biweekly-contest-27/problems/course-schedule-iv/

from typing import List
from functools import lru_cache
import collections

class Solution:
  def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]],
                          queries: List[List[int]]) -> List[bool]:
    if not prerequisites: return [False] * len(queries)


    g = collections.defaultdict(set)
    for a,b in prerequisites:
      g[b].add(a)

    @lru_cache(maxsize=None)
    def query(a, b):
      if a == b:
        return False

      if b in g[a]:
        return True

      return any(query(c, b) for c in g[a])


    return [query(b, a) for a,b in queries]

s = Solution()
#s.checkIfPrerequisite(n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]])
#s.checkIfPrerequisite(n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]])
#s.checkIfPrerequisite(n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]])
print(
  s.checkIfPrerequisite(

  n = 5,
  prerequisites=[[4,3],[4,1],[4,0],[3,2],[3,1],[3,0],[2,1],[2,0],[1,0]],
  queries=[[1,4],[4,2],[0,1],[4,0],[0,2],[1,3],[0,1]]

)
)


