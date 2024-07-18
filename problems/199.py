"""
Binary Tree Right Side View

Given the root of a binary tree,
imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
"""

from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS: Left to right
# Time: O(n) Space: O(n)
def rightSideView(root: Optional[TreeNode]) -> list[int]:
    res = []
    q = collections.deque([root] if root else [])
    while q:
        lastNode = None
        for _ in range(len(q)):
            lastNode = q.popleft()
            if lastNode.left: q.append(lastNode.left)
            if lastNode.right: q.append(lastNode.right)
        res.append(lastNode.val)
    return res
