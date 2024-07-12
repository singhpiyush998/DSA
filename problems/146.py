"""
LRU Cache

Design a data structure that follows the constraints of
a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists.
- Otherwise, add the key-value pair to the cache.
- If the number of keys exceeds the capacity from this operation,
- evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""

class Node:
    def __init__(self, key, val) -> None:
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> node

        # dummy nodes, left -> LRU, right -> Most Recently used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # insert at right (MRU)
    def insert(self, node: Node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    # Remove from list
    def remove(self, node: Node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # update the lru and mru
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            # remove LRU from list and delete it from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
