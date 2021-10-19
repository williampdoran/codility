# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next
        result = ListNode(-1)
        start = result
        while stack:
            # print(stack.pop())
            result.next = ListNode(stack.pop())
            result = result.next
        return start.next
