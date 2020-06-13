
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
      if not root: return []
      res = []
      self.helper(root, res)
      return res

    def helper(self, root, res):
      if root:
        if root.left: self.helper(root.left, res)
        res.append(root.val)
        if root.right: self.helper(root.right, res)


# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

# class Solution:
#   def preorderTraversal(self, root: TreeNode) -> List[int]:
#     if not root: return []
#     res = []
#     self.helper(root, res)
#     return res
#
#   def helper(self, root, res):
#     if root:
#       res.append(root.val)
#       if root.left: self.helper(root.left, res)
#       if root.right: self.helper(root.right, res)

# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

# class Solution:
#   def postorderTraversal(self, root: TreeNode) -> List[int]:
#     res = []
#     if not root: return res
#     self.helper(root, res)
#     return res
#
#   def helper(self, root, res):
#     if root:
#       if root.left: self.helper(root.left, res)
#       if root.right: self.helper(root.right, res)
#       res.append(root.val)