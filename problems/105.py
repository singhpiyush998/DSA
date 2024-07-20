"""
Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where
preorder is the preorder traversal of a binary tree and
inorder is the inorder traversal of the same tree,
construct and return the binary tree.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(nlogn) Space: O(n^2)
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None

        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
