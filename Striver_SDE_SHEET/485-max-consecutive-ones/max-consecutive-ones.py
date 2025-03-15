class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prefix = 0
        ans = 0
        for i in nums:
            if i==0:
                ans = max(ans,prefix)
                prefix = 0
            prefix+=i
        
        return max(ans,prefix)