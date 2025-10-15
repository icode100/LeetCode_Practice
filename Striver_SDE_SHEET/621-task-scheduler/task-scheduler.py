class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = list()
        for key,val in Counter(tasks).items(): heappush(heap,-val)
        q = deque()
        time = 0
        while heap or q:
            time+=1
            if heap:
                freq = heappop(heap)
                freq+=1
                if freq!=0: q.append([freq,time+n])
            if q and q[0][1]==time: heappush(heap,q.popleft()[0])
        return time
