class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        miss = [i for i in range(n) if s1[i]!=s2[i]]
        if len(miss)&1: return -1
        @cache
        def recursion(i,j):
            if i>j: return 0
            return min(min(miss[i+1]-miss[i],x)+recursion(i+2,j), min(miss[j]-miss[j-1],x)+recursion(i,j-2), min(miss[j]-miss[i],x)+recursion(i+1,j-1))
        return recursion(0,len(miss)-1)
            


            
