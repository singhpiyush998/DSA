"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains
a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(n) Space: O(1)
# def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#     # Find the size of both lists
#     size1 = 0
#     curr = l1
#     while curr:
#         curr = curr.next
#         size1 += 1

#     size2 = 0
#     curr = l2
#     while curr:
#         curr = curr.next
#         size2 += 1

#     # Add both lists until the shorter one
#     dummy = ListNode()
#     temp = dummy
#     ptr1, ptr2 = l1, l2
#     carry = 0
#     for _ in range(min(size1, size2)):
#         sum = ptr1.val + ptr2.val + carry
#         temp.next = ListNode((sum % 10))
#         carry = sum // 10
#         ptr1, ptr2 = ptr1.next, ptr2.next
#         temp = temp.next

#     # Add the rest of the values
#     curr = ptr1 or ptr2
#     while curr:
#         sum = curr.val + carry
#         temp.next = ListNode(sum % 10)
#         carry = sum // 10
#         temp = temp.next
#         curr = curr.next
#     if carry: temp.next = ListNode(carry)

#     return dummy.next

# Time: O(n) Space: O(1)
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    dummy = ListNode()
    curr = dummy
    while l1 or l2 or carry:
        opd1 = l1.val if l1 else 0
        opd2 = l2.val if l2 else 0
        sum = opd1 + opd2 + carry
        curr.next = ListNode(sum % 10)
        carry = sum // 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        curr = curr.next

    return dummy.next


l1 = ListNode(3, ListNode(7))
l2 = ListNode(9, ListNode(2))

total = addTwoNumbers(l1, l2)

curr = total
while curr:
    print(curr.val)
    curr = curr.next
