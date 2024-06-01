"""
if the node we are deleting has:
i) 0 Child -> Just delete it.
ii) 1 Child -> Just delete it and make its child, its parent's child
iii) 2 Childs
        ->(Find min in right subtree, copy the value in targetted node, Delete duplicate from right subtree)
        ->(Find max in left subtree, copy the value in targetted node, Delete duplicate from left subtree)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findMin(root: Node) -> Node:
    if root.left is None:
        return root
    return findMin(root.left)


def delete(root: Node, data: int) -> Node:
    if root is None:
        return root
    elif data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        # Found the node
        # case 1: No child
        if root.left is None and root.right is None:
            del root
            root = None
        # case 2: 1 child
        elif root.left is None or root.right is None:
            temp = root
            root = root.left or root.right
            del temp
        # case 3: 2 child
        else:
            temp = findMin(root.right)
            root.data = temp.data
            root.right = delete(root.right, temp.data)
        return root


def levelOrder(root: Node):
    if root is None:
        return

    discovered = [root]
    while len(discovered) > 0:
        node = discovered.pop(0)
        print(node.data, end=" ")  # visiting the node
        if node.left:
            discovered.append(node.left)
        if node.right:
            discovered.append(node.right)


root = Node(12)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(3)
root.left.right = Node(7)

root.right.left = Node(13)
root.right.right = Node(17)

root.left.left.left = Node(1)
root.left.right.right = Node(9)

levelOrder(root)
print()

delete(root, 5)
levelOrder(root)
print()
