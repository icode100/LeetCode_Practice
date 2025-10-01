class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sum = numBottles
        while numBottles>=numExchange:
            res,rem = numBottles//numExchange, numBottles%numExchange
            sum+=res
            numBottles = res+rem
        return sum

