class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        x = 0
        ans = list()

        for num in nums:
            
            x = x<<1
            x|=num
            ans.append(x%5==0)
        
        return ans