class Solution:
    def twoEggDrop(self, n: int) -> int:
        @cache
        def recursion(e,f):
            if e==1: return f
            if f==0 or f==1: return f
            return min([1+max(recursion(e-1,j-1),recursion(e,f-j)) for j in range(1,f+1)])
        return recursion(2,n)