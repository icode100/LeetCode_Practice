class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        p = 0
        ans = 0
        prev = 0
        prevcap = capacity
        check = set(passengers)
        for b in buses:
            cap = capacity
            while cap and p<len(passengers) and passengers[p]<=b:
                cap-=1
                if p==0 or passengers[p]-1>passengers[p-1]:
                    ans = passengers[p]-1
                p+=1
            if cap!=0 and (p==0 or b>passengers[p-1]): 
                ans = b
            # if cap!=0: ans = b
        return ans
            



