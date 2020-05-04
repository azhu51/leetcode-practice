
# https://leetcode-cn.com/problems/counting-bits/
# https://leetcode-cn.com/problems/counting-bits/solution/pythonti-jie-man-zu-mian-shi-de-liang-chong-si-lu-/

class Solution(object):
  def countBits(self, num):
    """
    :type num: int
    :rtype: List[int]
    """

    result = [0] * (num + 1)
    for i in range(1, num+1):
      if 1 & i:
        result[i] = result[i-1] + 1
      else:
        result[i] = result[i//2]

    return result


s = Solution()
s.countBits(5)