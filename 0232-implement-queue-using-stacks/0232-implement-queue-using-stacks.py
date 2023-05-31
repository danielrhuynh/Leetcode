class MyQueue:
    
    # The idea here is that we dont actually remove from the stack, we just
    # increment our pointer to the head of the 'queue' when we pop, and also
    # use the pointer to check if the queue has caught up to the end of the array and
    # is 'empty'. Although we are bleeding memory using this method
    def __init__(self):
        self.stack = []
        self.index = 0
        
    def push(self, x: int) -> None:
        return self.stack.append(x)

    def pop(self) -> int:
        self.index += 1
        return self.stack[self.index-1]

    def peek(self) -> int:
        return self.stack[self.index]

    def empty(self) -> bool:
        return self.index >= len(self.stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()