class Solution:
    def minSubArrayLen(self, x: int, arr: List[int]) -> int:
        N = len(arr)
        l = 0
        ans = N+1
        current = 0
        for r in range(N):
            current+=arr[r]
            while current>=x:
                ans = min(ans,r-l+1)
                current-=arr[l]
                l+=1
        return ans if ans!=(N+1) else 0