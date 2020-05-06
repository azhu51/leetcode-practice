
# https://leetcode-cn.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  def isValidBST(self, root: TreeNode) -> bool:

    def helper(node, lower=float('-inf'), upper=float('inf')):
      if not node:
        return True

      val = node.val
      print(val, lower, upper)
      if val <= lower or val >= upper:
        return False
      if not helper(node.right, val, upper):
        return False
      if not helper(node.left, lower, val):
        return False
      return True

    return helper(root)


s = Solution()
left = TreeNode(1)
right = TreeNode(3)
root = TreeNode(2)
root.left = left
root.right = right
s.isValidBST(root)