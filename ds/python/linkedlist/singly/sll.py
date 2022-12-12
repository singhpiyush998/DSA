
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
        prev = None
        curr = self.head
        for _ in range(0, index):
            prev = curr
            curr = curr.next
        
        # if loop doesn't run -> index - 0 -> prev = None
        if prev is None:
            node.next = self.head
            self.head = node
        else:
            node.next = prev.next
            prev.next = node

    def deleteAtIndex(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Invalid index")

        # 0 <= index < len(self)
        prev = None
        curr = self.head
        for _ in range(0, index):
            prev = curr
            curr = curr.next
        
        # if loop doesn't run -> index = 0 -> prev = None
        if prev is None:
            res = self.head.data
            self.head = self.head.next
        else:
            res = curr.data
            prev.next = curr.next

        return res


def main():
    sll = LinkedList()
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
    print(sll.deleteAtIndex(len(sll) - 1))
    print(sll)
    print(f"Length: {len(sll)}")
    print(sll.deleteAtIndex(0))
    print(sll)
    print(f"Length: {len(sll)}")
    print(sll.deleteAtIndex(2))
    print(sll)
    print(f"Length: {len(sll)}")
    print(sll.deleteAtTail())
    print(sll)
    print(sll.deleteAtTail())
    print(sll)
    print(sll.deleteAtTail())
    print(sll)

if __name__ == "__main__":
    main()
