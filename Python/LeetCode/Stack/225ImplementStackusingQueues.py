class MyStack:

    def __init__(self):
        self.queue = []
        self.queue_help = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        self.queue_help = self.queue[::-1]
        poped = self.queue_help[0]
        self.queue = self.queue_help[1:][::-1]
        return poped

    def top(self) -> int:
        self.queue_help = self.queue[::-1]
        top = self.queue_help[0]
        return top

    def empty(self) -> bool:
        return len(self.queue) ==0