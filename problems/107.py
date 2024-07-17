"""
Binary Tree Level Order Traversal II

Given the root of a binary tree, return the bottom-up level order traversal
of its nodes' values.
(i.e., from left to right, level by level from leaf to root).
"""

import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) Space: O(n)
def levelOrderBottom(root: Optional[TreeNode]) -> list[list[int]]:
    if not root: return []

    res = []
    queue = collections.deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(level)
    return res[::-1]


# Time: O(n) Space: O(n)
# def levelOrderBottom(root: Optional[TreeNode]) -> list[list[int]]:
#     res = collections.deque()
#     queue = collections.deque([root] if root else [])
#     while queue:
#         level = []
#         for _ in range(len(queue)):
#             node = queue.popleft()
#             level.append(node.val)
#             if node.left: queue.append(node.left)
#             if node.right: queue.append(node.right)
#         res.insert(0, level)

#     return list(res)
