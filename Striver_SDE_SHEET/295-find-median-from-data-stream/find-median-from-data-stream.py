class MedianFinder:

    def __init__(self):
        self.lheap = list()
        self.rheap = list()
        self.counter = 0
    def addNum(self, num: int) -> None:
        if self.counter%2==0:
            if self.rheap and num > -self.lheap[0] and num > self.rheap[0]:
                heappush(self.rheap,num)
                heappush(self.lheap,-heappop(self.rheap))
            else:
                heappush(self.lheap,-num)
            self.counter+=1
        else:
            if num < -self.lheap[0]:
                heappush(self.lheap,-num)
                heappush(self.rheap,-heappop(self.lheap))
            else:
                heappush(self.rheap,num)
            self.counter+=1

    def findMedian(self) -> float:
        if len(self.lheap)==len(self.rheap):
            return (-self.lheap[0]+self.rheap[0])/2
        else:
            return -self.lheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()