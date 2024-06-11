"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode
class where the right child
pointer points to the next node in the list
and the left child pointer is always null.
The "linked list" should be in the same order as a
pre-order traversal of the binary tree.

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
"""


from queue import SimpleQueue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    """
    recursively go through left subtree

    recursively go through right subtree

    fix the pointer in parent by setting parent's right as root of
    left subtree and parent's left as none and left subtree's
    leaf's right as parents' right
    """


class Solution:
    # def flatten(self, root: Optional[TreeNode]) -> None:
    #     if root is None:
    #         return
    #     self.flatten(root.left)
    #     self.flatten(root.right)
    #     if root.left:
    #         temp = root.right
    #         root.right = root.left
    #         curr = root.left
    #         while curr.right:
    #             curr = curr.right
    #         curr.right = temp
    #         root.left = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(root):
            if root is None:
                return None

            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None

            last = rightTail or leftTail or root
            return last
        dfs(root)


def levelorder(root):
    queue = SimpleQueue()
    queue.put(root)
    while not queue.empty():
        curr = queue.get()
        print(curr.val, end=" ")
        if curr.left:
            queue.put(curr.left)
        if curr.right:
            queue.put(curr.right)
    print()


def linkedListPrint(root):
    curr = root
    while curr:
        print(curr.val, end=" ")
        curr = curr.right
    print()


def main():
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(5)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    # root.left.left.right = TreeNode(0)
    # root.left.right.left = TreeNode(8)
    # root.left.right.right = TreeNode(9)
    # root.right.right = TreeNode(6)
    # root.right.left = TreeNode(7)

    # root = TreeNode()

    root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    Solution().flatten(root)

    levelorder(root)
    linkedListPrint(root)


if __name__ == "__main__":
    main()
