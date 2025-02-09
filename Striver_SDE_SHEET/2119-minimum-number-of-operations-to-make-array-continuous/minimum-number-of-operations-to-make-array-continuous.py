class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        j = 0
        finums = sorted(set(nums))
        for i in range(len(nums)):
            while j<len(finums) and finums[j]<finums[i]+n:
                j+=1
            ans = max(ans,j-i)
        return n-ans
        
