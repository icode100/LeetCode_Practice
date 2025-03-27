class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i,n = 0,len(heights)
        heap = list()
        while i<n:
            while i+1<n and heights[i]>=heights[i+1]: i+=1
            # print(i)
            if i==n-1: return i
            heappush(heap,(heights[i+1]-heights[i]))
            if len(heap)>ladders:
                if heap[0]<=bricks: bricks-=heappop(heap)
                else: return i
            i+=1
        return i