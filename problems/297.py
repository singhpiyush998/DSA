"""
Serialize and Deserialize Binary Tree

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization
algorithm should work. You just need to ensure that a
binary tree can be serialized to a string and this string
can be deserialized to the original tree structure.
"""

import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "X"
        return str(root.val) + "," + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = collections.deque(data.split(','))
