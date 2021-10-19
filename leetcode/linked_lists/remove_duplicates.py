# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        result = ListNode(-1)
        start = result
        current = head
        while current and current.next:
            if current.val == current.next.val:
                pass
            else:
                current.val < current.next.val
                result.next = ListNode(current.val)
                result = result.next
            current = current.next
        if current.val != result.val:
            result.next = ListNode(current.val)
        return start.next