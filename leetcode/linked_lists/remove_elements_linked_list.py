# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = ListNode(-1)
        start = result
        current = head
        while current:
            if current.val == val:
                pass
            else:
                result.next = ListNode(val=current.val)
                result = result.next
            current = current.next
            # print(f"c= {current} r={start}")

        return start.next