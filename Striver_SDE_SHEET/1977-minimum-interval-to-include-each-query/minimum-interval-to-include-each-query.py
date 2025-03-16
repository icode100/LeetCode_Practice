class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap = list()
        ans = {}
        i=0
        for q in sorted(queries):
            while i<len(intervals) and intervals[i][0]<=q: 
                s,e = intervals[i]
                heappush(heap,[e-s+1,e])
                i+=1
            while heap and heap[0][1]<q: 
                heappop(heap)
            ans[q] = heap[0][0] if heap else -1
        return [ans[q] for q in queries]

        

