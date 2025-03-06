class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days.sort()
        numday = [1,7,30]
        @cache
        def recursion(i):
            if i>=len(days): return inf
            ans = inf
            for j,c in enumerate(costs):
                find = days[i]+numday[j]
                idx = bisect_left(days,find)
                if idx==len(days): ans = min(ans,c)
                else: ans = min(ans,c+recursion(idx))
            return ans
        return recursion(0)
                
