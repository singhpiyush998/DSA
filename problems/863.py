"""
All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node,
and an integer k, return an array of the values of all nodes
that have a distance k from the target node.
You can return the answer in any order.
"""

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Convert tree to graph and apply bfs to the target's neighbours
# which are (parent, left child, right child)
def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
    # Find the parents of every node so we can traverse back/up the tree
    childToParent = {}
    q = collections.deque([root] if root else [])
    while q:
        node = q.popleft()
        if node.left:
            q.append(node.left)
            childToParent[node.left] = node
        if node.right:
            q.append(node.right)
            childToParent[node.right] = node

    # BFS from our target in all 3(up, left, right) directions upto k distance
    visited = set()
    q.append(target)
    visited.add(target)
    level = 0 # keep tracks of how far we are from the target node
    while q:
        if level == k: break
        for _ in range(len(q)):
            node = q.popleft()
            if node not in visited:
                visited.add(node)
            if node.left and node.left not in visited:
                q.append(node.left)
            if node.right and node.right not in visited:
                q.append(node.right)
            if node in childToParent and childToParent[node] not in visited:
                q.append(childToParent[node])
        level += 1

    # Iterate through the items left in the queue and return them as result
    return [node.val for node in q]
