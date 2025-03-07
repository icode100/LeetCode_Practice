class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[n][target] = 1
        for i in range(n-1,-1,-1):
            for c in range(-1000,1001):
                dp[i][c] = dp[i+1][c+nums[i]]+dp[i+1][c-nums[i]]
        return dp[0][0]
