class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N:int = len(customers)
        suffixSum:int = sum(list(map(lambda x: int(x=='Y'), customers)))
        currentSum:int = 0
        minPenalty:int = suffixSum
        ans:int = 0

        for i,c in enumerate(list(customers)):
            value = int(c!='Y')
            currentSum += value
            suffixSum -= (1-value)
            penalty:int = currentSum+suffixSum

            if minPenalty > penalty:
                minPenalty = penalty
                ans = i+1
        
        return ans


