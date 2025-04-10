class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def leq(x):
            if len(s)==len(x): return 1 if x>=s else 0
            if len(s)>len(x): return 0

            N = len(x)-len(s)
            
            ans = 0
            for i in range(N):
                if int(x[i])<=limit: ans += int(x[i]) * pow((limit+1),(N-i-1))
                else: 
                    ans += pow((limit+1),(N-i))
                    return ans
            if x[N:]>=s: ans+=1
            return ans
        
        return leq(str(finish)) - leq(str(start-1))




            