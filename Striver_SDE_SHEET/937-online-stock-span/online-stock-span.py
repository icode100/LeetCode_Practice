class StockSpanner:

    def __init__(self):
        self.stack = list()
        self.index = -1
    def next(self, price: int) -> int:
        self.index+=1
        while self.stack and self.stack[-1][0]<=price:
            self.stack.pop()
        ans = self.index-(-1 if not self.stack else self.stack[-1][1])
        self.stack.append([price,self.index])
        return ans
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)