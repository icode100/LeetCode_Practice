class Solution:
    def maxScore(self, A: List[int], B: List[int], k: int) -> int:
        N = len(A)
        pairs = sorted(zip(A,B),key=lambda x:-x[1])
        heap = list()
        ans = 0
        sum = 0
        for a,b in pairs:
            heappush(heap,a)
            sum+=a
            while len(heap)>k:
                sum-=heappop(heap)
            if len(heap)==k:ans = max(ans,sum*b)
        return ans


        