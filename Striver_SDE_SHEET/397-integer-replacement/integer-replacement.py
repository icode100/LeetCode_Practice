class Solution:
    def integerReplacement(self, n: int) -> int:
        @cache
        def recursion(n):
            if n==1: return 0
            if n&1:
                return 1+min(recursion(n-1), recursion(n+1))
            else: return 1+recursion(n>>1)
        return recursion(n)
