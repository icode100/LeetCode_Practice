class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        N:int = len(prices)
        if N==1: return 1
        l:int = 0
        count:int = 0

        calculatePeriod: Callable[[int],int] = lambda x: (x*(x+1))//2

        for r in range(1,N+1):
            r:int
            
            if r==N or prices[r-1]-1!=prices[r]:
                count+=calculatePeriod(r-l)
                l = r
        
        return count

            