# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        current = head
        pointer = head
        index = 0
        while(pointer.next and pointer.next.next):
            print(index, current.val, pointer.val)
            current = current.next
            pointer = pointer.next.next
            if current == pointer:
                return True
            index +=1
        return False
