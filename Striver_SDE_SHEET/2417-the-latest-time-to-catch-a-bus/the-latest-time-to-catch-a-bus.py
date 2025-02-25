class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers = deque(sorted(passengers))
        ans = -1
        vis = set()
        for b in buses:
            # if passengers[0]>b: continue
            c = capacity
            while passengers and c and passengers[0]<=b:
                if passengers[0]-1 not in vis: ans = max(ans,passengers[0]-1)
                vis.add(passengers.popleft())
                c-=1
            if c!=0:
                if b not in vis: ans = max(ans,b)
        return ans