class MyCalendarTwo:

    def __init__(self):
        self.hashmap = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        if startTime not in self.hashmap: self.hashmap[startTime] = 0
        if endTime not in self.hashmap: self.hashmap[endTime] = 0
        self.hashmap[startTime]+=1
        self.hashmap[endTime]-=1
        count = 0
        for i in self.hashmap:
            count+=self.hashmap[i]
            if count>=3:
                self.hashmap[startTime]-=1
                self.hashmap[endTime]+=1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)