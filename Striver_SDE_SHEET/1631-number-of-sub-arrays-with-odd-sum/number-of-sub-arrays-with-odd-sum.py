class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        N = len(arr)
        even,odd = 1,0
        ans = 0
        current = 0
        mod = int(1e9+7)
        for i in range(N):
            current+=arr[i]
            if current&1: 
                odd+=1
                ans+=even
            else:
                even+=1
                ans+=odd
        return ans%mod
        