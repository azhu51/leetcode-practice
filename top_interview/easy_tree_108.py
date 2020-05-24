# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
      def helper(left, right):
        if left > right:
          return None

        p = (left + right) // 2

        root = TreeNode(nums[p])
        root.left = helper(left, p - 1)
        root.right = helper(p+1, right)
        return root

      return helper(0, len(nums) - 1)

# simi problem
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/

