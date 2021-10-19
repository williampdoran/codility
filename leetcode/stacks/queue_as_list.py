class MyQueue:

    def __init__(self):
        self.capactiy = 100
        self.size = 0
        self.start = 0
        self.queue = [0]*self.capactiy

    def push(self, x: int) -> None:
        self.queue[(self.start +self.size) % self.capactiy] = x
        self.size += 1

    def pop(self) -> int:
        elem = self.queue[self.start % self.capactiy]
        self.start +=1
        self.size -= 1
        return elem

    def peek(self) -> int:
        return self.queue[self.start % self.capactiy]

    def empty(self) -> bool:
        return self.size == 0