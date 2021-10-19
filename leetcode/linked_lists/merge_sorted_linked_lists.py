# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left = l1
        right = l2
        if left == None:
            return right
        elif right == None:
            return left
        else:
            result = ListNode()
            start = result
            if left.val >= right.val:
                result.val=right.val
                right = right.next
            elif left.val < right.val:
                result.val=left.val
                left = left.next
            while(left and right):
                if left.val >= right.val:
                    result.next=ListNode(right.val)
                    right = right.next
                elif right.val > left.val :
                    result.next=ListNode(left.val)
                    left = left.next
                result = result.next
            if left:
                result.next = left
            elif right:
                result.next = right
            # print(f"result {start}, left {left}, right {right}")
            return start