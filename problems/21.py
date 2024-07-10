"""
Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(m + n) Space: O(1)
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummyNode = ListNode()
    tail = dummyNode
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2
    return dummyNode.next


def printList(ls: Optional[ListNode]):
    while ls:
        print(ls.val, end = " ")
        ls = ls.next
    print()

list1 = ListNode(1, ListNode(5, ListNode(6)))
list2 = ListNode(2, ListNode(3, ListNode(4)))

mergedList = mergeTwoLists(list1, list2)
printList(mergedList)
