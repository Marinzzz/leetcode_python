import queue
class MaxQueue:
    def __init__(self):
        self.myqueue = queue.Queue()
        self.helpqueue = queue.deque()

    def max_value(self) -> int:
        return self.helpqueue[0] if self.helpqueue else -1

    def push_back(self, value: int) -> None:
        while self.helpqueue and self.helpqueue[-1] < value:
            self.helpqueue.pop()
        self.helpqueue.append(value)
        self.myqueue.put(value)

    def pop_front(self) -> int:
        if not self.helpqueue:
            return -1
        value = self.myqueue.get()
        if value == self.helpqueue[0]:
            self.helpqueue.popleft()
        return value



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()