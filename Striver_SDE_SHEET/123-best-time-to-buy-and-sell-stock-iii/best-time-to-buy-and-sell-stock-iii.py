class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def recursion(index,clear,trans):
            if trans==0: return 0
            if index==n: return 0
            buy = 0
            skip = 0
            sell = 0
            skip = recursion(index+1,clear,trans)
            if clear:
                buy = -prices[index]+recursion(index+1,False,trans)
            else:
                sell = +prices[index]+recursion(index+1,True,trans-1)
            return max(skip,buy,sell)
        return recursion(0,True,2)