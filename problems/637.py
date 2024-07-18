"""
Average of Levels in Binary Tree

Given the root of a binary tree, return the average value of the nodes
on each level in the form of an array.
Answers within 10^-5 of the actual answer will be accepted.
"""

from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root: Optional[TreeNode]) -> list[float]:
    res = []
    q = collections.deque([root] if root else [])
    while q:
        sum, length = 0, len(q)
        for _ in range(len(q)):
            node = q.popleft()
            sum += node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(sum / length)
    return res
