# https://leetcode-cn.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
      if head is None: return False
      if head.next is None: return True

      p = head
      q = head.next

      while q and q.next:
        p = p.next
        q = q.next.next
        if p == q:
          return True


      return False

