class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = max(counter.keys())
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            pick = counter[i] * i + (dp[i - 2] if i - 2 >= 0 else 0)
            notpick = dp[i - 1] if i - 1 >= 0 else 0
            dp[i] = max(pick, notpick)
        return dp[n]


        
