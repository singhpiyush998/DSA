"""
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the
shortest path from the root node down to the nearest leaf node.
"""

from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS Solution
# Time: O(n) Space: O(n)
def minDepth(root: Optional[TreeNode]) -> int:
    if not root: return 0

    # bfs till a leaf is found and keep track of level
    q = collections.deque([(root, 0)])
    while q:
        node, level = q.popleft()
        if node:
            if not node.left and not node.right: return level + 1
            else:
                q.append((node.left, level + 1))
                q.append((node.right, level + 1))
