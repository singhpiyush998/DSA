"""
Subtree of Another Tree

Given the roots of two binary trees root and subRoot,
return true if there is a subtree of root with the
same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that
consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(m.n) Space: O(h)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode, q: TreeNode):
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
