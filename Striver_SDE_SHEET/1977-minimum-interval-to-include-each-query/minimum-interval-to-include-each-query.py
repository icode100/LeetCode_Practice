class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        intervals.sort()
        hashmap = defaultdict(int)
        heap = list()
        i = 0
        size = lambda x: (x[1]-x[0]+1)
        for q in sorted(queries):
            while i<n and intervals[i][0]<=q:
                heappush(heap, (size(intervals[i]),intervals[i][1]))
                i+=1
            while heap and heap[0][1]<q:
                heappop(heap)
            hashmap[q] = heap[0][0] if heap else -1
        
        return [hashmap[q] for q in queries]

