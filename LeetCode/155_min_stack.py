class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        TC: O(1)
        SC: O(1)
        """
        self.stack.append(val)

        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        """
        TC: O(1)
        SC: O(1)
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """
        TC: O(1)
        SC: O(1)
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        TC: O(1)
        SC: O(1)
        """
        return self.min_stack[-1]


def call(coms, vals):
    """
    TC: O(n)
    SC: O(n)
    """
    output = []
    min_stack = None
    for i, command in enumerate(coms):
        if command == "MinStack":
            min_stack = MinStack()
            output.append(None)
        elif command == "push":
            min_stack.push(vals[i][0])
            output.append(None)
        elif command == "pop":
            min_stack.pop()
            output.append(None)
        elif command == "top":
            output.append(min_stack.top())
        elif command == "getMin":
            output.append(min_stack.getMin())
    return output

coms = ["MinStack","push","push","getMin","getMin","push","getMin","getMin","top","getMin","pop","push","push","getMin","push","pop","top","getMin","pop"]
vals = [[],[-10],[14],[],[],[-20],[],[],[],[],[],[10],[-7],[],[-7],[],[],[],[]]
call(coms, vals)
