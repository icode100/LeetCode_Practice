class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        C = len(cost)
        N = len(cost)
        value = [c for c in cost]
        weight = list(map(lambda x:x+1,time))
        
        @cache
        def dp(i,C):
            if C<=0: return 0
            if i<0: return inf

            return min(
                value[i]+dp(i-1,C-weight[i]) if C-weight[i]>=0 else value[i], #pick 
                dp(i-1,C) # not-pick
            )
        return dp(N-1,C)