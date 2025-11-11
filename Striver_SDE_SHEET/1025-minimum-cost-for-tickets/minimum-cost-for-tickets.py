class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        @cache
        def rec(index):
            if index>=N: return int(1e9)
            ans = int(1e9)
            for i,cost in zip([1,7,30],costs):
                idx = bisect_left(days,days[index]+i)
                ans = min(ans,cost) if idx==N else min(ans,cost+rec(idx))
            return ans
        return rec(0)
