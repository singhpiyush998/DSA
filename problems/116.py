"""
Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children.

The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.
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


# Time: O(n) Space: O(n)
# def connect(root: Optional[Node]) -> Optional[Node]:
#     if not root: return None

#     q = collections.deque([(root, 0)])
#     while q:
#         node, level = q.popleft()
#         if q:
#             n, l = q[0]
#             if l == level: # if the node at the front of the list at the same level as current node, the set it as next
#                 node.next = n
#         if node.left:
#             q.append((node.left, level + 1))
#             q.append((node.right, level + 1))

#     return root

# BFS: Right to left
# Space: O(n) Time: O(n)
# def connect(root: Optional[Node]) -> Optional[Node]:
#     if not root: return None

#     q = collections.deque([root])
#     while q:
#         rightNode = None
#         for _ in range(len(q)):
#             node = q.popleft()
#             node.next, rightNode = rightNode, node
#             if node.right: # check if queue has "a" child, if one then both i.e not leaf as perfect btree
#                 q.append(node.right)
#                 q.append(node.left)

#     return root


# Time: O(n) Space: O(1)
def connect(root: Optional[Node]) -> Optional[Node]:
    curr, next = root, root.left if root else None

    while curr and next:
        curr.left.next = curr.right
        if curr.next:
            curr.right.next = curr.next.left

        curr = curr.next
        if not curr:
            curr = next
            next = curr.left
    return root
