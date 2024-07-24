"""
Maximum Width of Binary Tree

Given the root of a binary tree,
return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between
the end-nodes (the leftmost and rightmost non-null nodes),
where the null nodes between the end-nodes that would
be present in a complete binary tree extending down to
that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.
"""

import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(n) Space: O(n)
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 1
        queue = collections.deque([(root, 0)])

        while queue:
            start, end = queue[0][1], queue[-1][1]
            self.res = max(self.res, (end - start + 1))
            for _ in range(len(queue)):
                node, index = queue.popleft()
                leftChildIndex, rightChildIndex = 2 * index + 1, 2 * index + 2

                if node.left: queue.append((node.left, leftChildIndex))
                if node.right: queue.append((node.right, rightChildIndex))

        return self.res
