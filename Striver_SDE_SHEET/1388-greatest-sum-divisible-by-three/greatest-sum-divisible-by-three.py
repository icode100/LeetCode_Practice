class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        N = len(nums)
        
        dp = [0,0,0]
        dp[1] = dp[2] = -inf

        for i in range(N):
            copydp = dp.copy()
            for mod in range(3):

                notpick = dp[mod]
                pick = nums[i]+dp[(mod+(nums[i]%3))%3]
                copydp[mod] = max(notpick,pick)

            dp = copydp.copy()

        return dp[0] if dp[0]!=-inf else 0


        

    
            
            
        