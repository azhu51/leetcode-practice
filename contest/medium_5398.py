
# https://leetcode-cn.com/contest/biweekly-contest-26/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def goodNodes(self, root: TreeNode) -> int:
    if not root: return 0
    self.ans = 0
    def solver(root, cur):
      if not root: return
      if root.val>=cur:
        self.ans += 1
      cur = max(cur, root.val)
      solver(root.left, cur)
      solver(root.right, cur)

    solver(root, -10 ** 9)
    return self.ans

