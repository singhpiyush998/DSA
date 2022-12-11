
class LinkedList:
    def __init__(self):
        self.head = None

    class __Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    @classmethod
    def getNewNode(cls, data):
        return cls.__Node(data)

    def insertAtHead(self, node):
        node.next = self.head
        self.head = node

    def deleteAtHead(self):
        if self.head is None:
            return False

        self.head = self.head.next
        return True

    def insertAtTail(self, node):
        if ( tmp := self.head ) is None:
            self.head = node
        else:
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = node

    def deleteAtTail(self):
        if ( tmp := self.head ) is None:
            return False

        if tmp.next is None:
            self.head = None
        else:
            while tmp.next.next is not None:
                tmp = tmp.next
            tmp.next = None
        return True

    def length(self):
        i = 0
        tmp = self.head
        while tmp is not None:
            tmp = tmp.next
            i += 1
        return i

    def insertAtIndex(self, node, index):
        if index < 0 or index > self.length():
            return False

        # 0 <= index <= self.length()
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
        if index < 0 or index >= self.length():
            return False

        # 0 <= index < self.length()
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

        return False

    def display(self):
        if (( tmp := self.head ) is None):
            return False

        while tmp is not None:
            print(tmp.data, end = " ")
            tmp = tmp.next
        print()
        return True


def main():
    sll = LinkedList()
    # returns true if operation is successfull else false
    sll.insertAtHead(LinkedList.getNewNode(6))
    sll.insertAtHead(LinkedList.getNewNode(5))
    sll.insertAtHead(LinkedList.getNewNode(3))
    sll.display() # 3 4 5
    print(f"Length: {sll.length()}")
    sll.insertAtTail(LinkedList.getNewNode(7))
    sll.display()
    print(f"Length: {sll.length()}")
    sll.insertAtIndex(LinkedList.getNewNode(2), 0)
    sll.display()
    print(f"Length: {sll.length()}")
    sll.insertAtIndex(LinkedList.getNewNode(4), 2)
    sll.display()
    print(f"Length: {sll.length()}")
    sll.deleteAtIndex(sll.length() - 1)
    sll.display()
    print(f"Length: {sll.length()}")
    sll.deleteAtIndex(0)
    sll.display()
    print(f"Length: {sll.length()}")
    sll.deleteAtIndex(2)
    sll.display()
    print(f"Length: {sll.length()}")

if __name__ == "__main__":
    main()
