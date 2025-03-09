class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = abs(n)
        def recursion(n):
            if n==0: return 1
            if n&1: return x*recursion(n-1)
            else: return recursion(n>>1)**2
        return recursion(n)