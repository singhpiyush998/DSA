"""
Diameter of Binary Tree

Given the root of a binary tree,
return the length of the diameter of the tree.
The diameter of a binary tree is the length of the
longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is
represented by the number of edges between them.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # the language is a bit confusing, we actually have to
    # find the longest path that exists in the tree
    # diameter = 2 + height of left subtree + height of right subtree
    # height = 1 + max(left, right)
    # Time: O(n) Space: O(n)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root: return -1

            leftSubTreeHeight = dfs(root.left)
            rightSubTreeHeight = dfs(root.right)

            res = max(res, 2 + leftSubTreeHeight + rightSubTreeHeight)
            return 1 + max(leftSubTreeHeight, rightSubTreeHeight)

        dfs(root)
        return res
