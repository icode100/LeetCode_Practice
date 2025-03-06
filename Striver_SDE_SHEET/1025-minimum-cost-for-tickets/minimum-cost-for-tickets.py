class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days.sort()
        numday = [1,7,30]
        dp = [inf for _ in range(len(days)+1)]
        for i in range(len(days)-1,-1,-1):
            for j,c in enumerate(costs):
                find = days[i]+numday[j]
                idx = bisect_left(days,find)
                # print(idx)
                if idx >= len(days): dp[i] = min(dp[i],c)
                else: dp[i] = min(dp[i], c+dp[idx])
        return dp[0]
                
