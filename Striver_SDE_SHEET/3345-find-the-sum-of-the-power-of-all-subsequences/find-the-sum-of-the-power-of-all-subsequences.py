class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        mod = int(1e9+7)
        N = len(nums)
        
        @cache
        def recursion(i,current,M):
            if current==0:
                return ((1<<(N-M)))%mod
            if i==N:
                return 0
            
            return sum(
                [
                    recursion(i+1,current,M),
                    recursion(i+1,current-nums[i],M+1) if nums[i]<=current else 0
                ]
            )%mod
        
        return recursion(0, k, 0)