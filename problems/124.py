"""
Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair
of adjacent nodes in the sequence has an edge connecting them.
A node can only appear in the sequence at most once.
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res
            if not root: return 0

            leftPathSum = dfs(root.left)
            rightPathSum = dfs(root.right)

            maximum = root.val + max(leftPathSum, rightPathSum, leftPathSum + rightPathSum, 0)
            res = max(res, maximum)
            return root.val + max(leftPathSum, rightPathSum, 0)

        dfs(root)
        return res
