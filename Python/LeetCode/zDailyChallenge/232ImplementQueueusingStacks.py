class MyQueue:

    def __init__(self):
        self.queue = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        self.stack2 = self.queue[::-1]
        temp = self.stack2.pop()
        self.queue = self.stack2[::-1]
        return temp

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
