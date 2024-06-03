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
