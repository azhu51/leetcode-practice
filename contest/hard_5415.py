
# https://leetcode-cn.com/contest/weekly-contest-189/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

from typing import List
import math

class Solution:
  def numPoints(self, points: List[List[int]], r: int) -> int:
    ans = 0
    rr = r ** 2
    for [x1, y1] in points:
      for [x2, y2] in points:
        num = 0
        x0, y0 = x1, y1
        if x2 != x0 or y2 != y0:
          dx, dy = (x2 - x1), (y2 - y1)
          temp = dx ** 2 + dy ** 2
          if temp <= rr * 4:
            # 方向变换
            dx, dy = -dy, dx
            R = math.sqrt(rr - temp / 4)
            x0 = (x1 + x2) / 2 + R * dx / math.sqrt(temp)
            y0 = (y1 + y2) / 2 + R * dy / math.sqrt(temp)
        for [x3, y3] in points:
          if (x3 - x0) ** 2 + (y3 - y0) ** 2 <= rr:
            num += 1
        ans = max(ans, num)
    return ans
