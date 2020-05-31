# https://leetcode-cn.com/problems/count-primes/


# https://leetcode-cn.com/problems/count-primes/solution/ru-he-gao-xiao-pan-ding-shai-xuan-su-shu-by-labula/

# 素数的定义很简单，如果一个数如果只能被 1 和它本身整除，那么这个数就是素数。

# Sieve of Eratosthenes


class Solution:
  def countPrimes(self, n: int) -> int:
    isPrim = [True for _ in range(n)]


    for i in range(2, n):
      if isPrim[i]:
        for j in range(2 * i, n, i):
          isPrim[j] = False

    count = 0

    for i in range(2, n):
      if isPrim[i]:
        count = count + 1

    return count


s = Solution()
s.countPrimes(10)
