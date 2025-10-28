class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        p = 0
        ans = 0
        vis = set()
        for b in buses:
            cap = 0
            while p<len(passengers) and passengers[p]<=b and cap<capacity:
                if passengers[p]-1 not in vis: ans = max(passengers[p]-1,ans)
                vis.add(passengers[p])
                p+=1
                cap+=1
            if cap<capacity and b not in vis: ans = max(ans,b)
        return ans

