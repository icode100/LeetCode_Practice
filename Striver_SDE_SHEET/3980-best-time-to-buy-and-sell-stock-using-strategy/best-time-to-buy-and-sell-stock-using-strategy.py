class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        N:int = len(prices)
        purePrefix: List[int] = list(accumulate(prices))
        stratPrefix: List[int] = list()
        stratSuffix: List[int] = list()

        current:int = 0
        for i in range(N):
            current+=(strategy[i]*prices[i])
            stratPrefix.append(current)
        
        current = 0
        for i in range(N-1,-1,-1):
            current+=(strategy[i]*prices[i])
            stratSuffix.append(current)
        
        stratSuffix = stratSuffix[::-1]

        ans:int = stratPrefix[-1]

        for i in range(N-k+1):
            prefixSum = 0 if i==0 else stratPrefix[i-1]
            suffixSum = 0 if i==N-k else stratSuffix[i+k]

            changeSum = purePrefix[i+k-1]-purePrefix[i+(k//2)-1]

            ans = max(ans,prefixSum+suffixSum+changeSum)
        
        return ans