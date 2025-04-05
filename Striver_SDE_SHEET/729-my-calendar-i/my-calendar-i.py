class MyCalendar:

    def __init__(self):
        self.map = SortedDict()

    def book(self, s: int, e: int) -> bool:
        self.map[s] = self.map.get(s,0)+1
        self.map[e] = self.map.get(e,0)-1
        flag = True
        count = 0
        for i,v in self.map.items():
            count+=v
            if count>1: 
                flag = False
                break
        if not flag: 
            self.map[s]-=1
            self.map[e]+=1
        # print(self.map)
        return flag
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)