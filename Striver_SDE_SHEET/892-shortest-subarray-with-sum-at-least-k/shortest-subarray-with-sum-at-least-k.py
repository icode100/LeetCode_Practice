class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        heap = list()
        current = 0
        ans = inf
        for i,num in enumerate(nums):
            current+=num
            if current>=k:
                ans = min(ans,i+1)
            while heap and current-heap[0][0]>=k:
                val,idx = heappop(heap)
                ans = min(ans,i-idx)
            heappush(heap,[current,i])
        return -1 if ans == inf else ans