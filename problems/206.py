from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Iterative, Time: O(n) Space: O(1)
# def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
#     curr = head
#     prev = None
#
#     while curr:
#         temp = curr.next
#         curr.next = prev
#         prev = curr
#         curr = temp
#     head = prev
#
#     return head

# Recursive, Time: O(n) Space: O(n)
def reverseList(
        curr: Optional[ListNode],
        prev: Optional[ListNode]
) -> Optional[ListNode]:
    if curr is None:
        return prev
    temp = curr.next
    curr.next = prev
    return reverseList(temp, curr)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head = reverseList(head, None)
while head:
    print(head.val, end=" ")
    head = head.next

print()
