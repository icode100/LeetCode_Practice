class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        sum = numBottles
        while numBottles>=numExchange:
            numBottles-=numExchange
            numExchange+=1
            numBottles+=1
            sum+=1
        return sum