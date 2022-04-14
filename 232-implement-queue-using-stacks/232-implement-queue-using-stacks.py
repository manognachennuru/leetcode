class MyQueue:

    def __init__(self):
        from collections import deque
        self.stk = deque() #stack used to implement queue
        self.front = 0
        self.rear = -1

    def push(self, x: int) -> None:
        self.stk.append(x)
        self.rear += 1

    def pop(self) -> int:
        frontVal = self.stk[self.front]
        self.front += 1
        return frontVal

    def peek(self) -> int:
        return self.stk[self.front]

    def empty(self) -> bool:
        return self.front > self.rear


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()