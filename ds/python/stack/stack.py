
class Stack:
    class __Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    def __iter__(self):
        temp = self.top
        while temp:
            yield temp.data

    def __repr__(self):
        return f"Stack({', '.join(str(node) for node in self)})"

    def __len__(self):
        return len(tuple(iter(self)))

    @classmethod
    def getNewNode(cls, data):
        return cls.__Node(data)

    def push(self, node):
        node.next = self.top
        self.top = node

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")

        res = self.top
        self.top = self.top.next
        return res.data

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")

        return self.top.data

    def isEmpty(self):
        return self.top is None


def main():
    stack = Stack()
    stack.push(Stack.getNewNode("Harry Potter"))
    print(stack, f"\nLength: {len(stack)}")
    stack.push(Stack.getNewNode("The Hobbit"))
    print(stack, f"\nLength: {len(stack)}")
    stack.push(Stack.getNewNode("Lord of the rings"))
    print(stack, f"\nLength: {len(stack)}")
    print(f"\n{stack.pop()} is removed from stack")
    print(stack, f"\nLength: {len(stack)}")
    print(f"\n{stack.pop()} is removed from stack")
    print(stack, f"\nLength: {len(stack)}")
    print(f"\n{stack.pop()} is removed from stack")
    print(stack, f"\nLength: {len(stack)}")

if __name__ == "__main__":
    main()

