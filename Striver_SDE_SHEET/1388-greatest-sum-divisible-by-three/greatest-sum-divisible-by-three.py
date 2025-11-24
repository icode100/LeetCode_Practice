class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def recursion(index,mod):

            if index<0: 
                return 0 if mod==0 else -inf

            notpick = recursion(index-1,mod)
            pick = nums[index]+recursion(index-1,(mod+(nums[index]%3))%3)

            return max(pick,notpick)

        ans = recursion(N-1,0)
        return ans if ans != -inf else 0

    
            
            
        