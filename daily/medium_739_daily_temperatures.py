
# https://leetcode-cn.com/problems/daily-temperatures/
from typing import List

class Solution:
  # 超时
  def dailyTemperaturesI(self, T: List[int]) -> List[int]:
    copyT = T

    arr = []
    for j in range(0, len(T)):
      tmp = []
      for i in range(j+1, len(copyT)):
        tmp.append(T[i] - T[j])
        if(T[i] - T[j])>0:
          break
      arr.append(tmp)

    ans = []

    for elem in arr:
      ans.append(0)
      for j in range(0, len(elem)):
        if elem[j] > 0:
          ans.pop()
          ans.append(j+1)
          break


    return ans

  def dailyTemperaturesII(self, T: List[int]) -> List[int]:
    n = len(T)

    ans, nxt, big = [0] * n, dict(), 10 ** 9

    for i in range(n - 1, -1, -1):
      warmer_index = min(nxt.get(t, big) for t in range(T[i] + 1, 102))
      if warmer_index != big:
        ans[i] = warmer_index - i
      nxt[T[i]] = i

    return ans

  def dailyTemperaturesIII(self, T: List[int]) -> List[int]:
    length = len(T)
    ans = [0] * length
    stack = []
    for i in range(length):
      temperature = T[i]
      while stack and temperature > T[stack[-1]]:
        prev_index = stack.pop()
        ans[prev_index] = i - prev_index
      stack.append(i)
    return ans






s = Solution()
s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
