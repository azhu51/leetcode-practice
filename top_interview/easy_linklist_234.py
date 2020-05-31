# https://leetcode-cn.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
      if not head: return True
      ans = []
      p = head
      ans.append(p.val)
      while p and p.next:
        p = p.next
        ans.append(p.val)


      return ans == ans[::-1]


