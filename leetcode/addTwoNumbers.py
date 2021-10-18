# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"ListNode: {self.val} -> {self.next} "


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_left = l1
        current_right = l2
        sum = current_left.val + current_right.val
        carry = sum // 10
        start = ListNode(val= sum % 10)
        result_node = start
        current_left = current_left.next if current_left else None
        current_right = current_right.next if current_right else None
        while current_left or current_right:
            if current_left and current_right:
                sum = current_left.val + current_right.val + carry
                carry = sum // 10
            elif current_left:
                sum = current_left.val + carry
                carry = sum // 10
            else:
                sum = current_right.val + carry
                carry = sum // 10
            result_node.next = ListNode(val = sum % 10)
            result_node = result_node.next
            current_left = current_left.next if current_left else None
            current_right = current_right.next if current_right else None
        if(carry == 1):
            result_node.next = ListNode(val = carry)
        return start

# list1 = ListNode(val = 2, next = ListNode(val = 4, next = ListNode(3)))
# list2 = ListNode(val = 5, next = ListNode(val = 6, next = ListNode(4)))
#
# print("Solution", Solution().addTwoNumbers(list1, list2))

list1 = ListNode(val = 9, next = ListNode(val = 9))
list2 = ListNode(val = 1)

print("Solution", Solution().addTwoNumbers(list1, list2))