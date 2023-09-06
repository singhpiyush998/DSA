import sys

sys.path.insert(0, "../ds/python/linkedlist/")
from singly.sll import LinkedList
#
# def isPalindrome(head):
#     # mid = head
#     # end = head
#     # m, n = 0,0
#     # while True:
#     #     end = end.next.next
#     #     mid = mid.next
#     #     m += 1
#     #     n += 2
#     #     if not end:
#     #         break
#     #     if not end.next:
#     #         n += 1
#     #         break
#     #
#     
#     # print("Len: ", n)
#     # print(f"Mid: {mid.data}")
#     # print(f"Mid index: {m}")
#     # print(f"After mid: {afterMid.data}")
#     
#     len = 0
#     tmp = head
#     while tmp:
#         len +=1
#         tmp = tmp.next
#         
#     midIndex = len // 2
#     mid = head
#     for i in range(midIndex):
#         mid = mid.next
#         
#     afterMid = mid.next if len % 2 else mid
#     i = 1
#     while afterMid:
#         beforeMid = head
#         for _ in range(i, mid):
#             beforeMid = beforeMid.next
#         if beforeMid.data != afterMid.data:
#             return False
#         afterMid = afterMid.next
#         i += 1
#     return True

from collections import deque

# def isPalindrome(head):
#     stack = deque()
#     tmp = head
#     n = 0
#     while tmp:
#         stack.append(tmp)
#         tmp = tmp.next
#         n += 1
#
#     midIndex = n // 2
#     
#     temp = head
#     for _ in range(midIndex):
#         if temp.data != stack.pop().data:
#             return False
#         temp = temp.next
#
#     return True

# def isPalindrome(head):
#     stack = deque()
#     tmp = head
#     n = 0
#     while tmp:
#         stack.appendleft(tmp.data)
#         tmp = tmp.next
#         n += 1
#
#     tmp = head
#     for _ in range(n // 2):
#         if tmp.data != stack.popleft():
#             return False
#         tmp = tmp.next
#
#     return True

def isPalindrome(head):
    mid, end = head, head
    
    while end and end.next:
        end, mid = end.next.next, mid.next

    prev, next, mid.next = mid, mid.next, None

    while next:
        next.next, prev, next = prev, next, next.next

    while prev:
        if head.data != prev.data:
            return False
        head, prev = head.next, prev.next

    return True
    
def main():
    sll = LinkedList()
    sll.insertAtTail(LinkedList.getNewNode(1))
    sll.insertAtTail(LinkedList.getNewNode(2))
    sll.insertAtTail(LinkedList.getNewNode(1))
    sll.insertAtTail(LinkedList.getNewNode(1))
    sll.insertAtTail(LinkedList.getNewNode(1))
    print(sll)
    print(isPalindrome(sll.head))

if __name__ == "__main__":
    main()
