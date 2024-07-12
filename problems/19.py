"""
Remove Nth Node From End of List

Given the head of a linked list,
remove the nth node from the end of the list
and return its head.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time: O(n) Space: O(1)
# def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
#     # Find the size of the list
#     size = 0
#     temp = head
#     while temp:
#         size += 1
#         temp = temp.next

#     # iterate to (size - n)th element(previous of target) of the list
#     dummy = ListNode(next=head)
#     temp = dummy
#     for i in range(size - n):
#         temp = temp.next

#     # delete its next element
#     temp.next = temp.next.next
#     return dummy.next

# Time: O(n) (1 pass) O(1)
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(next=head)
    l = dummy
    r = head
    for _ in range(n):
        r = r.next

    while r:
        l, r = l.next, r.next
    l.next = l.next.next

    return dummy.next


ls = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ls = removeNthFromEnd(ls, 5)

temp = ls
while temp:
    print(temp.val)
    temp = temp.next
