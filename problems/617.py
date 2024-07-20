"""
Merge Two Binary Trees

You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.
You need to merge the two trees into a new binary tree.
The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) Space: O(n)
def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(node1, node2):
        if not node1 and not node2: return

        if node1 and node2:
            node = TreeNode(node1.val + node2.val)
            node.left = dfs(node1.left, node2.left)
            node.right = dfs(node1.right, node2.right)
        else:
            node = node1 or node2
        return node
    return dfs(root1, root2)
