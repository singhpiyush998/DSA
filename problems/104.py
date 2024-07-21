"""
Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the farthest leaf node.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Bottom up approach
    # Time: O(n) Space: O(h)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        leftSubtreeDepth = self.maxDepth(root.left)
        rightSubtreeDepth = self.maxDepth(root.right)
        return max(leftSubtreeDepth, rightSubtreeDepth) + 1

    # Top-down approach
    # Time: O(n) Space: O(h)
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     res = 0
    #     def dfs(root, level):
    #         if not root: return None
    #         nonlocal res
    #         res = max(res, level + 1)
    #         dfs(root.left, level + 1)
    #         dfs(root.right, level + 1)

    #     dfs(root, 0)
    #     return res
