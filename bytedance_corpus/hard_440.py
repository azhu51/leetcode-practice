
# https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/

class Solution:
  # 超时
  def findKthNumberI(self, n: int, k: int) -> int:
    tmp = []
    for i in range(1, n+1):
      tmp.append(str(i))

    return int(sorted(tmp)[k-1])

  def findKthNumber(self, n: int, k: int) -> int:
    cur = 1
    prefix = 1

    while cur < k :
      print(prefix, n)
      cnt  = self.get_count(prefix, n)
      print(cnt,cur)
      if cur + cnt > k:
        prefix *= 10
        cur += 1
      else:
        prefix += 1
        cur += cnt
        # print(cnt, prefix)

    return prefix

  def get_count(self, i, n):
    if i <= n:
      cnt = 1
    else:
      return 0
    a = i
    b = i + 1
    while True:
      a = a * 10
      b = b * 10
      if n >= b:
        cnt += b - a
      elif n >= a:
        cnt += n - a + 1
      else:
        break
    return cnt


s = Solution()
s.findKthNumber(20,3)