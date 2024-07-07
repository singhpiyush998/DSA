"""
Min Stack

Design a stack that supports push, pop, top, and retrieving the 
minimum element in constant time.

Implement the MinStack class:
    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""

# class MinStack:
#     def __init__(self):
#         self.data = []
#         self.minimum = 2 ** 31
#
#     def push(self, val: int) -> None:
#         self.minimum = min(self.minimum, val)
#         self.data.append((val, self.minimum))
#
#     def pop(self) -> None:
#         val = self.data.pop()
#         if val[0] == self.minimum:
#             if self.data:
#                 self.minimum = self.data[-1][1]
#             else:
#                 self.minimum = 2 ** 31
#
#     def top(self) -> int:
#         return self.data[-1][0]
#
#     def getMin(self) -> int:
#         return self.data[-1][1]

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        currMin = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(currMin)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
