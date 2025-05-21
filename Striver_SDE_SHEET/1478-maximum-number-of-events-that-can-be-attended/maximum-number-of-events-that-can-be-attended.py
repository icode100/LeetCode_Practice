class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort()
        heap = list()
        i,count = 0,0
        for d in range(1,int(1e5)+1):
            while heap and heap[0]<d: heappop(heap)
            while i<N and events[i][0]<=d: 
                heappush(heap,events[i][1])
                i+=1
            if heap and heap[0]>=d: 
                count+=1
                heappop(heap)
        return count