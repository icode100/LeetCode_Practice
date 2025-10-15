class MedianFinder:

    def __init__(self):
        self.container = SortedList()

    def addNum(self, num: int) -> None:
        self.container.add(num)
        

    def findMedian(self) -> float:
        N = len(self.container)
        if N&1:
            return self.container[N//2]
        else:
            return (self.container[(N//2)-1]+self.container[N//2])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()