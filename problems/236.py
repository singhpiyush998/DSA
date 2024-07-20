"""
Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA)
of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
The lowest common ancestor is defined between two nodes p and q as
the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).
"""

from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Time: O(n) Space: O(h)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: return None
        if root == p or root == q:
            return root

        leftSearchResult = self.lowestCommonAncestor(root.left, p, q)
        rightSearchResult = self.lowestCommonAncestor(root.right, p, q)

        if leftSearchResult and rightSearchResult:
            return root
        return leftSearchResult or rightSearchResult
