class Solution:
    def myPow(self, x: float, n: int) -> float:
        x,n = (x,n) if n>=0 else (1/x,-n)
        if n==0: return 1
        ans = 1
        while n:
            if n&1: 
                ans*=x
                n-=1
            else: 
                x*=x
                n = n>>1
        return ans
