class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0]-x[1])
        ans = 0
        for i,(a,b) in enumerate(costs):
            ans+= (a if i<(len(costs)>>1) else b)
        return ans
