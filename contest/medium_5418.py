
# https://leetcode-cn.com/contest/weekly-contest-190/problems/pseudo-palindromic-paths-in-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def pseudoPalindromicPaths(self, root: TreeNode) -> int:
    res = []
    from collections import Counter
    def helper(root, lst):
      if not root: return
      if not root.left and not root.right:
        res.append(lst+[root.val])
      elif not root.left:
        helper(root.right, lst+[root.val])
      elif not root.right:
        helper(root.left, lst+[root.val])
      else:
        helper(root.right, lst+[root.val])
        helper(root.left, lst+[root.val])

    helper(root,[])
    ans = 0
    for i in res:
      dic = Counter(i)
      single = 0
      for i in dic:
        if dic[i] % 2 !=0:
          single+=1
      if single <= 1:
        ans+=1
    return ans


