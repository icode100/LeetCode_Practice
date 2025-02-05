class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        k = 0
        ans,heap = 0,list()
        for i in range(1,int(1e5)+1):
            while heap and heap[0]<i: heappop(heap)
            while k<len(events) and events[k][0]<=i: 
                heappush(heap,events[k][1])
                k+=1
            if heap and heap[0]>=i:
                ans+=1
                heappop(heap)
        return ans
        