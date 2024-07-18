"""
Populating Next Right Pointers in Each Node II

Given a binary tree,
Populate each next pointer to point to its next right node.
If there is  no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
"""

import collections
from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# BFS: Right to left
# Time: O(n) Space: O(n)
# def connect(root: Node) -> Node:
#     q = collections.deque([root] if root else [])
#     while q:
#         rightPointer = None
#         for _ in range(len(q)):
#             node = q.popleft()
#             node.next, rightPointer = rightPointer, node
#             if node.right: q.append(node.right)
#             if node.left: q.append(node.left)

#     return root

# BFS left to right with dummy node technique
# Time: O(n) Space: O(n)
# def connect(root: Node) -> Node:
#     q = collections.deque([root] if root else [])
#     while q:
#         prev = Node()
#         for _ in range(len(q)):
#             curr = q.popleft()
#             prev.next, prev = curr, curr

#             if curr.left: q.append(curr.left)
#             if curr.right: q.append(curr.right)
#     return root

# while iterating a level, we connect all the nodes of its next level
# We iterate the next level like a linked list
# Time : O(n) Space: O(1)
def connect(root: Node) -> Node:
    curr = root
    while curr:
        dummy = Node()
        child = dummy

        while curr:
            if curr.left:
                child.next, child = curr.left, curr.left
            if curr.right:
                child.next, child = curr.right, curr.right
            curr = curr.next
        curr = dummy.next

    return root
