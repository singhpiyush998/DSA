
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

    def deleteAtHead(self):
        if (tmp := self.head) is None:
            raise Exception("Linked List is empty")

        self.head = self.head.next
        return True

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
            self.head = None
        else:
            while tmp.next.next is not None:
                tmp = tmp.next
            tmp.next = None
        return True

    def insertAtIndex(self, node, index):
        if index < 0 or index > len(self):
            raise IndexError("Invalid index")

        # 0 <= index <= len(self)
        prev = None
        curr = self.head
        for _ in range(0, index):
            prev = curr
            curr = curr.next
        
        # if loop doesn't run -> prev = None
        if prev is None:
            node.next = self.head
            self.head = node
        else:
            node.next = prev.next
            prev.next = node

        return True

    def deleteAtIndex(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Invalid index")

        # 0 <= index < len(self)
        prev = None
        curr = self.head
        for _ in range(0, index):
            prev = curr
            curr = curr.next
        
        # if loop doesn't run -> prev = None
        if prev is None:
            self.head = self.head.next
        else:
            prev.next = curr.next

        return True


def main():
    sll = LinkedList()
    # returns true if operation is successfull
    sll.insertAtHead(LinkedList.getNewNode(6))
    sll.insertAtHead(LinkedList.getNewNode(5))
    sll.insertAtHead(LinkedList.getNewNode(3))
    print(sll) # 3 4 5
    print(f"Length: {len(sll)}")
    sll.insertAtTail(LinkedList.getNewNode(7))
    print(sll)
    print(f"Length: {len(sll)}")
    sll.insertAtIndex(LinkedList.getNewNode(2), 0)
    print(sll)
    print(f"Length: {len(sll)}")
    sll.insertAtIndex(LinkedList.getNewNode(4), 2)
    print(sll)
    print(f"Length: {len(sll)}")
    sll.deleteAtIndex(len(sll) - 1)
    print(sll)
    print(f"Length: {len(sll)}")
    sll.deleteAtIndex(0)
    print(sll)
    print(f"Length: {len(sll)}")
    sll.deleteAtIndex(2)
    print(sll)
    print(f"Length: {len(sll)}")

if __name__ == "__main__":
    main()
