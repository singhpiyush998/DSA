"""
An easy solution would be inorder traversal with Time complexity of O(n)
but we want to solve it in O(h)

Case 1: Node has right subtree
inorder successor of the node would be the left most node in the right subtree
or find min in the right subtree

Case 2: Node has no right subtree
The nearest ancestor for which the given node is in left subtree
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findMin(root: Node):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root


def search(root: Node,  data: int) -> bool:
    if root is None:
        return None
    if (root.data == data):
        return root
    elif data <= root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)


def getSuccessor(root: Node, data: int) -> Node:
    # search the node - O(h)
    current = search(root, data)
    if current is None:
        return None

    # Case1: if node has a right subtree
    if current.right is not None:
        return findMin(current.right)
    # Case2: if node has no right subtree
    else:
        # walk the tree from root till current and
        # find the deepest ancestor for which the current node is in left subtree
        successor = None
        ancestor = root
        while ancestor != current:
            if current.data < ancestor.data:  # this means that current is in left of the ancestor
                successor = ancestor
                ancestor = ancestor.left
            else:
                # current node lies to the right of ancestor
                ancestor = ancestor.right
        return successor


root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.left.left.left = Node(6)
root.left.right.left = Node(11)
root.right.left = Node(17)
root.right.left.left = Node(16)
root.right.right = Node(25)
root.right.right.right = Node(27)

print(f"Suceesor of 12 is {getSuccessor(root, 12).data}")
