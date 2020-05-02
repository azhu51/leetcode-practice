
#https://leetcode-cn.com/contest/biweekly-contest-25/problems/kids-with-the-greatest-number-of-candies/

from typing import List

class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int):

    max_candies = max(candies)

    res = []

    for i in range(0, len(candies)):
      if candies[i] + extraCandies >= max_candies:
        res.append(True)
      else:
        res.append(False)

    return res


s = Solution()
print(s.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))