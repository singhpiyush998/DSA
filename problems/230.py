"""
Kth Smallest Element in a BST

Given the root of a binary search tree,
and an integer k, return the kth smallest value (1-indexed)
of all the values of the nodes in the tree.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        rank = 0

        def dfs(root):
            nonlocal res, rank
            if not root:
                return

            dfs(root.left)
            rank += 1
            if rank == k:
                res = root.val
                return
            dfs(root.right)

        dfs(root)
        return res
