
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

      curA = headA
      curB = headB

      while curA!=curB:
        if curA:
          curA = curA.next
        else:
          curA = headB

        if curB:
          curB = curB.next
        else:
          curB = headA


      return curA


