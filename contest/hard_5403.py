
# https://leetcode-cn.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/submissions/

class Solution(object):
  def kthSmallest(self, mat, k):
    """
    :type mat: List[List[int]]
    :type k: int
    :rtype: int
    """

    m = len(mat)
    n = len(mat[0])
    res = mat[0]

    for i in range(1, m):
      temp = list()
      for r in res:
        for m1 in mat[i]:
          temp.append( r +m1)
      temp = sorted(temp)
      res = temp[:k]
    return res[-1]