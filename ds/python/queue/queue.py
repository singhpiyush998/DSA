
class Queue:
    class __Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.front = None
        self.rear = None

    def __iter__(self):
        temp = self.front
        while temp:
            yield temp.data
            temp = temp.next

    def __repr__(self):
        return f"Queue({', '.join(str(node) for node in self)})"

    def __len__(self):
        return len(tuple(iter(self)))

    @classmethod
    def getNewNode(cls, data):
        return cls.__Node(data)

    def enqueue(self, node):
        if self.rear is None:
            self.rear = node
            self.front = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")

        front = self.front
        self.front = self.front.next
        return front.data

    def getFront(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")

        return self.front.data

    def getRear(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")

        return self.rear.data

    def isEmpty(self):
        return self.front is None or self.rear is None


def main():
    queue = Queue()
    queue.enqueue(Queue.getNewNode("Eenne"))
    print(f"{queue}\nLength: {len(queue)}")
    queue.enqueue(Queue.getNewNode("Menne"))
    print(f"{queue}\nLength: {len(queue)}")
    queue.enqueue(Queue.getNewNode("Manne"))
    print(f"{queue}\nLength: {len(queue)}")
    print(f"\n{queue.dequeue()} removed from queue")
    print(f"{queue}\nLength: {len(queue)}")
    print(queue.getFront(), " at the front of queue")
    print(queue.getRear(), " at the back of queue")

if __name__ == "__main__":
    main()
