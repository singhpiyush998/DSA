"""
Path Sum III

Given the root of a binary tree and an integer targetSum,
return the number of paths where the
sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf,
but it must go downwards(i.e.,traveling only from parent nodes to child nodes).
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(n) Space: O(h)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        freq = {0:1} # maps Path Sum -> frequency
        def dfs(root, prevSum):
            if not root: return

            currSum = prevSum + root.val
            x = currSum - targetSum
            if x in freq:
                # even though that key is in the dictionary, its value can be 0
                # that's why we don't wanna blindly increment by 1
                self.count += freq[x]

            if currSum in freq:
                freq[currSum] += 1
            else:
                freq[currSum] = 1

            dfs(root.left, currSum)
            dfs(root.right, currSum)

            # we reduce the count of current sum so that in another path,
            # if we encounter the same current sum/x value, this one doesn't interfere with it.
            freq[currSum] -= 1

        dfs(root, 0)
        return self.count


    # def countPaths(self, root, targetSum) -> int:
    #     res = 0

    #     def dfs(root, targetSum):
    #         nonlocal res
    #         if not root: return 0

    #         targetSum -= root.val
    #         if targetSum == 0:
    #             res += 1
    #             return

    #         dfs(root.left, targetSum)
    #         dfs(root.right, targetSum)

    #     dfs(root, targetSum)
    #     return res

    # # Time: O(n^2) Space: O(h)
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    #     res = 0

    #     def dfs(root):
    #         nonlocal res
    #         if not root: return

    #         # how many paths from current node sum to targetSum
    #         count = self.countPaths(root, targetSum)
    #         res += count
    #         dfs(root.left)
    #         dfs(root.right)

    #     dfs(root)
    #     return res
