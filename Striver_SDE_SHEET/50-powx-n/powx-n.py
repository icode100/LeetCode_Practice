class Solution:
    def myPow(self, x: float, n: int) -> float:
        x,n = (x,n) if n>=0 else (1/x,-n)
        if n==0: return 1
        def recursion(x,n):
            if n==0: return 1
            if n&1: return x*recursion(x,n-1)
            else: return recursion(x,n>>1)**2
        return recursion(x,n)