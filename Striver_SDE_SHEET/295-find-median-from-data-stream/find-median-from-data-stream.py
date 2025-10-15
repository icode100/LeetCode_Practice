class MedianFinder:

    def __init__(self):
        self.left = list()
        self.right = list()

    def addNum(self, num: int) -> None:
        if (len(self.left)+len(self.right))&1==0:
            if self.left: leftmax = -self.left[0]
            if self.right: rightmin = self.right[0]
            if self.right and num > leftmax and num >rightmin:
                heappush(self.right,num)
                heappush(self.left,-heappop(self.right))
            else:
                heappush(self.left,-num) #because the median in case of odd length will be from left half
        else:
            if self.left: leftmax = -self.left[0]
            if self.right: rightmin = self.right[0]
            if num<leftmax:
                heappush(self.left,-num)
                heappush(self.right,-heappop(self.left))
            else:
                heappush(self.right,num)   

    def findMedian(self) -> float:
        if len(self.left)==len(self.right): return (-self.left[0]+self.right[0])/2
        else: return -self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()