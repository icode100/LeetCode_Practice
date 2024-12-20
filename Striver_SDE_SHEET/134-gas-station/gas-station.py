class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start,sum = 0,0
        gassum,costsum = 0,0
        for i in range(len(gas)):
            gassum+=gas[i]
            costsum+=cost[i]
            sum+=(gas[i]-cost[i])
            if sum<0:
                sum=0
                start = i+1
        return start if gassum>=costsum else -1