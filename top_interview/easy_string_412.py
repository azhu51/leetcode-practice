
# https://leetcode-cn.com/problems/fizz-buzz/

from typing import List

class Solution:
  def fizzBuzz(self, n: int) -> List[str]:
    res = []

    for i in range(n):
      if i % 3 == 0 and i % 5 == 0:
        res.append("FizzBuzz")
        continue
      if i % 3 == 0:
        res.append("Fizz")
        continue
      if i % 5 == 0:
        res.append("Buzz")
        continue
      res.append(str(i))

    return res


