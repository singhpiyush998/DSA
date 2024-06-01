class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Time: O(n) Space: O(n)
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


root = Node('F')
root.left = Node('D')
root.right = Node('J')
root.left.left = Node('B')
root.left.right = Node('E')
root.left.left.left = Node('A')
root.left.left.right = Node('C')
root.right.left = Node('G')
root.right.right = Node('K')
root.right.left.right = Node('I')
root.right.left.right.left = Node('H')

levelOrder(root)
print()
