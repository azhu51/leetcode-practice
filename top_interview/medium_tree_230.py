
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
      res = []
      if not root: return
      self.helper(root, res)
      return sorted(res)[k-1]


    def helper(self, root, res):
      if root:
        res.append(root.val)
        if root.left: self.helper(root.left, res)
        if root.right: self.helper(root.right, res)