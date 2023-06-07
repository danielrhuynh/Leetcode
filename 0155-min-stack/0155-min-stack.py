class MinStack:

    def __init__(self):
        self.stack = []
        self.sorted_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.sorted_stack[-1] if self.sorted_stack else val)
        self.sorted_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.sorted_stack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sorted_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()