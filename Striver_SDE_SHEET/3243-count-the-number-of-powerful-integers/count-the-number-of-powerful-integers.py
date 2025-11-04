class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        N = len(str(finish))
        prefix_length = N-len(s)
        start = str(start).zfill(N)
        finish = str(finish)
        @cache
        def recursion(index, ifstart, iffinish):
            if index==N: return 1
            low = int(start[index]) if ifstart else 0
            high = int(finish[index]) if iffinish else 9
            if index<prefix_length:
                ans = 0
                for num in range(low,min(high,limit)+1):
                    ans+=recursion(index+1, ifstart and num==low, iffinish and num==high)
                return ans
            val = int(s[index-prefix_length])
            if low<=val<=min(high,limit): 
                return recursion(index+1,ifstart and val==low, iffinish and val==high)  
            return 0
        
        return recursion(0,True,True)
                
