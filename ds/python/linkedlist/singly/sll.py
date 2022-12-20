
class LinkedList:
    class __Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.data
            temp = temp.next

    def __repr__(self):
        return f"LinkedList({', '.join(str(node) for node in self)})"

    def __len__(self):
        return len(tuple(iter(self)))

    @classmethod
    def getNewNode(cls, data):
        return cls.__Node(data)

    def insertAtHead(self, node):
        node.next = self.head
        self.head = node

    def removeAtHead(self):
        if (tmp := self.head) is None:
            raise Exception("Linked List is empty")

        self.head = self.head.next
        return tmp.data

    def insertAtTail(self, node):
        if (tmp := self.head) is None:
            self.head = node
        else:
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = node

    def deleteAtTail(self):
        if (tmp := self.head) is None:
            raise Exception("Linked List is empty")

        if tmp.next is None:
            res = self.head.data
            self.head = None
        else:
            while tmp.next.next is not None:
                tmp = tmp.next
            res = tmp.next.data
            tmp.next = None
        return res

    def insertAtIndex(self, node, index):
        if index < 0 or index > len(self):
            raise IndexError("Invalid index")

        # 0 <= index <= len(self)
        if index == 0:
            return self.insertAtHead(node)

        # 1 <= index <= len(self)
        prev = self.head
        for _ in range(1, index):
            prev = prev.next

        node.next = prev.next
        prev.next = node

    def removeAtIndex(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Invalid index")

        # 0 <= index < len(self)
        if index == 0:
            return self.removeAtHead()

        # 1 <= index < len(self)
        prev = self.head
        for _ in range(1, index):
            prev = prev.next

        res = prev.next.data
        prev.next = prev.next.next
        return res


def main():
    sll = LinkedList()
    sll.insertAtHead(LinkedList.getNewNode(6))
    sll.insertAtHead(LinkedList.getNewNode(5))
    sll.insertAtHead(LinkedList.getNewNode(3))
    print(sll) # 3 5 6
    print(f"Length: {len(sll)}\n")
    sll.insertAtTail(LinkedList.getNewNode(7))
    print(sll) # 3 5 6 7
    print(f"Length: {len(sll)}\n")
    sll.insertAtIndex(LinkedList.getNewNode(2), 0)
    print(sll) # 2 3 5 6 7
    print(f"Length: {len(sll)}\n")
    sll.insertAtIndex(LinkedList.getNewNode(4), 2)
    print(sll) # 2 3 4 5 6 7
    print(f"Length: {len(sll)}\n")
    print(sll.removeAtIndex(len(sll) - 1), "popped")
    print(sll) # 2 3 4 5 6
    print(f"Length: {len(sll)}\n")
    print(sll.removeAtIndex(0), "popped")
    print(sll) # 3 4 5 6
    print(f"Length: {len(sll)}\n")
    print(sll.removeAtIndex(2), "popped")
    print(sll) # 3 4 6
    print(f"Length: {len(sll)}\n")
    print(sll.deleteAtTail(), "popped")
    print(sll) # 3 4
    print(f"Length: {len(sll)}\n")
    print(sll.deleteAtTail(), "popped")
    print(sll) # 3
    print(f"Length: {len(sll)}\n")
    print(sll.deleteAtTail(), "popped")
    print(sll) # Blank
    print(f"Length: {len(sll)}\n")

if __name__ == "__main__":
    main()
