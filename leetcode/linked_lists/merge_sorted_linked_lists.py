# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}->{self.next}"


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

    def mergeTwoLists2(self, list1, list2):
            """
            :type list1: Optional[ListNode]
            :type list2: Optional[ListNode]
            :rtype: Optional[ListNode]
            """
            if list1==None:
                return list2
            elif list2==None:
                return list1
            else:
                start = ListNode()
                result = start
                l = list1
                r = list2
                while l and r:
                    if l.val <= r.val:
                        result.next = ListNode(l.val)
                        l = l.next
                    else:
                        result.next = ListNode(r.val)
                        r = r.next
                    result = result.next
                if l:
                    result.next = l
                elif r:
                    result.next = r
                return start.next

    def mergeTwoListsRecursive(self, list1, list2):
            if list1 == None:
                return list2
            elif list2 == None:
                return list1
            else:
                if list1.val >= list2.val:
                    list2.next = self.mergeTwoLists(list1, list2.next)
                    return list2
                elif list2.val > list1.val:
                    list1.next = self.mergeTwoLists(list1.next, list2)
                    return list1

L1 = ListNode(1, next=ListNode(2, ListNode(4)))
L2 = ListNode(1, next=ListNode(3, ListNode(4)))
print(L1)
print(L2)
print(Solution().mergeTwoLists(L1,L2))
print(Solution().mergeTwoLists2(L1,L2))
print(Solution().mergeTwoListsRecursive(L1,L2))