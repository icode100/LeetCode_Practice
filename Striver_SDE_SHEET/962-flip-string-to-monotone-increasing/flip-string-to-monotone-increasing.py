class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        @cache
        def recursion(i,hasone):
            if i==len(s): return 0
            if hasone:
                if s[i]=='0':
                    return 1+recursion(i+1,hasone)
                else:
                    return recursion(i+1,hasone)
            else:
                if s[i]=='0':
                    return min(1+recursion(i+1,True),recursion(i+1,False))
                else:
                    return min(1+recursion(i+1,False),recursion(i+1,True))
        
        return recursion(0,False)
