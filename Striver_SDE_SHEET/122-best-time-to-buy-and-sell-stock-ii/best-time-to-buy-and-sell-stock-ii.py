class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        @cache
        def recursion(index,flag):
            if index>=N: return 0
            if flag: return max(prices[index]+recursion(index+1,not flag),recursion(index+1,flag))
            else: return max(-prices[index]+recursion(index+1,not flag), recursion(index+1,flag))
        return recursion(0,False)
