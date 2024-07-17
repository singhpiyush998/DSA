"""
Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal
of its nodes' values. (i.e.,
from left to right, then right to left for the next level and alternate between)
"""

import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) Space: O(n)
def zigzagLevelOrder(root: Optional[TreeNode]) -> list[list[int]]:
    res = []
    q = collections.deque([root] if root else [])
    leftToRight = True
    while q:
        currLevel = []
        for _ in range(len(q)):
            node = q.popleft() if leftToRight else q.pop()
            currLevel.append(node.val)
            if leftToRight:
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            else:
                if node.right: q.appendleft(node.right)
                if node.left: q.appendleft(node.left)
        res.append(currLevel)
        leftToRight = not leftToRight

    return res

# Time: O(n) Space: O(n)
# def zigzagLevelOrder(root: Optional[TreeNode]) -> list[list[int]]:
#     res = []
#     queue = collections.deque([root] if root else [])
#     direction = 1
#     while queue:
#         level = []
#         for _ in range(len(queue)):
#             node = queue.popleft()
#             level.append(node.val)
#             if node.left:  queue.append(node.left)
#             if node.right: queue.append(node.right)

#         res.append(level[::direction])
#         direction *= -1

#     return res
