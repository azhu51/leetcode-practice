
# https://leetcode-cn.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
      if head == None or head.next == None: return head
      p = self.reverseList(head.next)
      head.next.next = head
      head.next = None
      return p

    def reverseListii(self, head:ListNode):
      prev = None
      curr = head
      while curr != None:
        nextTemp = curr.next
        curr.next = prev
        prev = curr
        curr = nextTemp

      return prev
