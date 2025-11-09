class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        weight = [t+1 for t in time]
        value = cost
        N = C = len(time)  
        @cache 
        def rec(i,C):
            if C<=0: return 0
            if i>=N: return int(1e9)
            return min(value[i]+rec(i+1,C-weight[i]) if weight[i]<=C else value[i],rec(i+1,C))
        return rec(0,C)