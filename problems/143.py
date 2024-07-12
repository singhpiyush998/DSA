"""
Reorder List

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes.
Only nodes themselves may be changed.
"""

# from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time: O(n) Space: O(n) (Recursion)
# def reorderList(head: ListNode) -> None:
#     # Find the middle of the list
#     mid, end = head, head.next
#     while end and end.next:
#         mid = mid.next
#         end = end.next.next
#     if end: mid = mid.next # if it was an even list, move mid to next posn

#     # Reverse the 2nd half of the list(from mid to end)
#     def rev(curr: ListNode, prev: Optional[ListNode]):
#         if not curr: return prev
#         temp = curr.next
#         curr.next = prev
#         return rev(temp, curr)
#     end = rev(mid, None)

#     # Iterate through the modified list to reorder
#     ptr1, ptr2 = head, end
#     while ptr2 and ptr1 != ptr2:
#         temp1, temp2 = ptr1.next, ptr2.next
#         ptr1.next = ptr2
#         if temp1 != ptr2: ptr2.next = temp1
#         ptr1, ptr2 = temp1, temp2

#     # TEST: Print the reordered list
#     while head:
#         print(head.val)
#         head = head.next

# Time: O(n) Space: O(1)
def reorderList(head: ListNode) -> None:
    # Find the middle of the list
    mid, end = head, head.next
    while end and end.next:
        mid = mid.next
        end = end.next.next

    # Reverse the 2nd half of the list(from mid + 1 to end)
    mid = mid.next
    end, prev = mid, None
    while end:
        temp = end.next
        end.next = prev
        end, prev = temp, end
    end = prev

    # Iterate through the modified list to reorder
    ptr1, ptr2 = head, end
    while ptr2:
        temp1, temp2 = ptr1.next, ptr2.next
        ptr1.next = ptr2
        ptr2.next = temp1
        ptr1, ptr2 = temp1, temp2
    ptr1.next = None

    # TEST: Print the reordered list
    while head:
        print(head.val)
        head = head.next

ls = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reorderList(ls)
