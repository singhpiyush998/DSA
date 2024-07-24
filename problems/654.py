"""
Maximum Binary Tree

You are given an integer array nums with no duplicates.

A maximum binary tree can be built recursively from nums
using the following algorithm:
Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the
subarray prefix to the left of the maximum value.
Recursively build the right subtree on the
subarray suffix to the right of the maximum value.

Return the maximum binary tree built from nums.
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(nlogn) Space: O(n)
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = sorted(enumerate(nums), key=lambda x: x[1])

        def dfs(nums):
            if not nums:
                return None

            index, val = stack.pop()
            root = TreeNode(val)
            root.left = self.constructMaximumBinaryTree(nums[:index])
            root.right = self.constructMaximumBinaryTree(nums[index + 1:])

            return root

        return dfs(nums)
