"""
Linked List Cycle

Given head, the head of a linked list,
determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list
that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node
that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time: O(n) Space: O(n)
# def hasCycle(self, head: Optional[ListNode]) -> bool:
#     ls = set()
#     curr = head
#     while curr:
#         if curr in ls:
#             return True
#         ls.add(curr)
#         curr = curr.next
#     return False

# Algorithm: Floyd's Tortoise and Hare
# Time: O(n) Space: O(1)
def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast: return True
    return False
