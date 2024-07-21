"""
Path Sum II

Given the root of a binary tree and an integer targetSum,
return all root-to-leaf paths where the sum of
the node values in the path equals targetSum.
Each path should be returned as a list of the node values,
not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        res = []

        def dfs(root, path, targetSum):
            if not root: return

            targetSum -= root.val
            if root.left is None and root.right is None:
                if targetSum == 0:
                    res.append(path + [root.val])
                return

            dfs(root.left, path + [root.val], targetSum)
            dfs(root.right, path + [root.val], targetSum)

        dfs(root, [], targetSum)
        return res
