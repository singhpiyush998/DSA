"""
Remove Duplicates from Sorted List

Given the head of a sorted linked list,
delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(n) Space: O(1)
def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    while curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head
