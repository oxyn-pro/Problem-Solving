from collections import deque

# Suppose your list is a queue, and according to the queue you can only start removing from
# the first value added (FIFO). In this case, the pop() method should still be O(n).


class MyStack2:
    """Used 1 queue to solve the problem"""

    def __init__(self):
        self.queue = deque()

    # TC: O(1)
    # SC: O(1)
    def push(self, x: int) -> None:
        self.queue.append(x)

    # TC: O(n)
    # SC: O(1)
    def pop(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

        return self.queue.popleft()

    # TC: O(n)
    # SC: O(1)
    def top(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

        res = self.queue.popleft()
        self.queue.append(res)
        return res

    # TC: O(1)
    # SC: O(1)
    def empty(self) -> bool:
        return not self.queue


class MyStack:
    """Used 2 queues to solve the problem"""

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    # TC: O(1)
    # SC: O(1)
    def push(self, x: int) -> None:
        self.queue1.append(x)

    # TC: O(n)
    # SC: O(1)
    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        res = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1

        return res

    # TC: O(n)
    # SC: O(1)
    def top(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        last_element = self.queue1[0]
        self.queue2.append(self.queue1.popleft())

        self.queue1, self.queue2 = self.queue2, self.queue1
        return last_element

    # TC: O(1)
    # SC: O(1)
    def empty(self) -> bool:
        return not self.queue1


obj = MyStack()
obj.push(1)
obj.push(2)
obj.top()
obj.pop()
obj.pop()
obj.empty()
