class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        diff = [gas[i]-cost[i] for i in range(N)]
        if sum(diff)<0: return -1
        start = 0
        sum_from_start = 0
        for i in range(N):
            sum_from_start+=diff[i]
            if sum_from_start<0:
                sum_from_start = 0
                start = i+1
        return start
        
