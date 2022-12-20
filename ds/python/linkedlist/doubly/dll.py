
class LinkedList:
    class __Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

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
        if self.head is not None:
            self.head.prev = node
            node.next = self.head

        self.head = node

    def insertAtTail(self, node):
        if (tmp := self.head) is None:
            self.head = node
        else:
            while tmp.next is not None:
                tmp = tmp.next
            node.prev = tmp
            tmp.next = node

    def removeAtHead(self):
        if (currHead := self.head) is None:
            raise Exception("Linked list is empty")

        if self.head.next is not None:
            self.head.next.prev = None

        self.head = self.head.next
        return currHead.data

    def removeAtTail(self):
        if (currHead := self.head) is None:
            raise Exception("Linked list is empty")

        if self.head.next is None:
            self.head = None
            return currHead.data

        tail = self.head
        while tail.next is not None:
            tail = tail.next

        tail.prev.next = None
        
        return tail.data

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

        node.prev = prev
        node.next = prev.next
        prev.next = node
        if nextNode := node.next:
            nextNode.prev = node


    def removeAtIndex(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Invalid index")

        # 0 <= index < len(self)
        if index == 0:
            return self.removeAtHead()

        # 1 <= index < len(self)
        toDelete = self.head.next
        for _ in range(1, index):
            toDelete = toDelete.next

        toDelete.prev.next = toDelete.next
        if toDelete.next:
            toDelete.next.prev = toDelete.prev
        return toDelete.data


    def reversePrint(self, node):
        if node is None:
            print("Reverse print: ")
            return
        self.reversePrint(node.next)
        print(node.data, end = " ")
        if node is self.head:
            print()


def main():
    dll = LinkedList()
    dll.insertAtHead(LinkedList.getNewNode(5))
    dll.insertAtHead(LinkedList.getNewNode(4))
    dll.insertAtHead(LinkedList.getNewNode(3))
    dll.insertAtTail(LinkedList.getNewNode(6))
    print(f"{dll}\nLength: {len(dll)}")
    dll.reversePrint(dll.head)
    print(f"\n{dll.removeAtHead()} removed from list")
    print(f"{dll}\nLength: {len(dll)}")
    dll.reversePrint(dll.head)
    dll.insertAtIndex(LinkedList.getNewNode(3), 0)
    print(f"{dll}\nLength: {len(dll)}")
    dll.reversePrint(dll.head)
    dll.insertAtIndex(LinkedList.getNewNode(7), len(dll))
    print(f"{dll}\nLength: {len(dll)}")
    dll.reversePrint(dll.head)
    dll.insertAtIndex(LinkedList.getNewNode("Middle"), 2)
    print(f"{dll}\nLength: {len(dll)}")
    dll.reversePrint(dll.head)
    print(f"\n{dll.removeAtTail()} removed from list")
    print(f"{dll}\nLength: {len(dll)}")
    dll.reversePrint(dll.head)
    print(f"\n{dll.removeAtIndex(2)} removed from list")
    print(f"{dll}\nLength: {len(dll)}")
    dll.reversePrint(dll.head)
    print(f"\n{dll.removeAtIndex(0)} removed from list")
    print(f"{dll}\nLength: {len(dll)}")
    dll.reversePrint(dll.head)
    print(f"\n{dll.removeAtIndex(len(dll) - 1)} removed from list")
    print(f"{dll}\nLength: {len(dll)}")
    dll.reversePrint(dll.head)

if __name__ == "__main__":
    main()
