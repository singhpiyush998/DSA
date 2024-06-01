class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBstUtil(root: Node, minValue: int, maxValue: int) -> bool:
    if root is None:
        return True
    if (root.data < maxValue and root.data > minValue and
        isBstUtil(root.left, minValue, root.left.data) and
            isBstUtil(root.right, root.right.data, maxValue)):
        return True
    else:
        return False


def isBST(root: Node):
    return isBstUtil(root, int('inf'), int('-inf'))
