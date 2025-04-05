class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        N = len(nums)
        even_suffix = [0]*(N+1)
        odd_suffix = [0]*(N+1)
        for i in range(N-1,-1,-1):
            if i&1: odd_suffix[i]+=nums[i]
            else: even_suffix[i]+=nums[i]
            even_suffix[i],odd_suffix[i] = even_suffix[i]+even_suffix[i+1], odd_suffix[i]+odd_suffix[i+1]
        even_prefix,odd_prefix,ans = 0,0,0
        for i in range(N):
            ans += int(even_prefix+odd_suffix[i+1] == odd_prefix+even_suffix[i+1])
            if i&1: odd_prefix+=nums[i]
            else: even_prefix+=nums[i]
        return ans
                

