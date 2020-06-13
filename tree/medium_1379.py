
# https://leetcode-cn.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

  def __init__(self):
    self.ans = None
    self.isFind = False

  def getTargetCopy(self, original: TreeNode, cloned: TreeNode,
                    target: TreeNode) -> TreeNode:
    if not original: return None
    if original == target: return cloned
    self.helper(original, cloned, target, self.ans, self.isFind)
    return self.ans

  def helper(self, original, cloned, target, ans, isFind):
    #   if original:
    if isFind:
      return
    if original == target:
      self.ans = cloned
      self.isFind = True
      return
    if original.left: self.helper(original.left, cloned.left, target, ans,
                                  isFind)
    if original.right: self.helper(original.right, cloned.right, target, ans,
                                   isFind)
