class MinStack:

    def __init__(self):
        self.stack = []
        self.topStack = -1

    def push(self, val: int) -> None:
        if self.topStack == -1:
            self.stack.append((val, val))
        else:
            minSoFar = self.stack[-1][1]
            self.stack.append((val, min(minSoFar, val) ))

        self.topStack += 1

    def pop(self) -> None:
        self.stack.pop()

        self.topStack -= 1

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()