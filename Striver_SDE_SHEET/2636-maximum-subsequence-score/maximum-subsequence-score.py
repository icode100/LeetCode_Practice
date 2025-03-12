class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n:int = len(nums1)
        pairs:list[tuple[int,int]]  = list(zip(nums1,nums2))
        pairs.sort(key = lambda x:(-x[1],-x[0]))
        sumi:int = 0
        heap:list[int] = list()
        for i in range(k):
            heapq.heappush(heap,pairs[i][0])
            sumi+=pairs[i][0]
        answer:int = sumi*pairs[k-1][1]

        for i in range(k,n):
            sumi-=heapq.heappop(heap)
            sumi+=pairs[i][0]
            heapq.heappush(heap,pairs[i][0])
            answer = max(answer,sumi*pairs[i][1])
        return answer


        