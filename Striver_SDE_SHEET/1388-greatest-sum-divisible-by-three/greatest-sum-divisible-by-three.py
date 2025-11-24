class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        N = len(nums)

        dp = [[0]*3 for _ in range(N+1)]
        dp[0][1] = dp[0][2] = -inf

        for i in range(1,N+1):
            for mod in range(3):
                notpick = dp[i-1][mod]
                pick = nums[i-1]+dp[i-1][(mod+(nums[i-1]%3))%3]
                dp[i][mod] = max(notpick,pick)
        
        return dp[N][0] if dp[N][0]!=-inf else 0


        # @cache
        # def recursion(index,mod):

        #     if index<0: 
        #         return 0 if mod==0 else -inf

        #     notpick = recursion(index-1,mod)
        #     pick = nums[index]+recursion(index-1,(mod+(nums[index]%3))%3)

        #     return max(pick,notpick)

        # ans = recursion(N-1,0)
        # return ans if ans != -inf else 0

    
            
            
        