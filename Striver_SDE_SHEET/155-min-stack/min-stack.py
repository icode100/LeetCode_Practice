class MinStack:
    def __init__(self):
        self.currentmin = inf
        self.stack = list()
    def push(self, val: int) -> None:
        self.currentmin = min(self.currentmin,val)
        self.stack.append((val,self.currentmin))
    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.currentmin = self.stack[-1][1]
        else:
            self.currentmin = inf
    def top(self) -> int:
        return self.stack[-1][0]
    def getMin(self) -> int:
        return self.stack[-1][1]