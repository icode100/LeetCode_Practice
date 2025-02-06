class MyCalendarThree:

    def __init__(self):
        self.hashmap = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.hashmap[startTime]=self.hashmap.get(startTime,0)+1
        self.hashmap[endTime]=self.hashmap.get(endTime,0)-1
        count = 0
        k = 0
        for i,v in self.hashmap.items():
            count+=v
            k = max(k,count)
        return k


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)