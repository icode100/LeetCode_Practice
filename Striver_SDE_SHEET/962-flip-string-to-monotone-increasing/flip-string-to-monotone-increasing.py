class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        N = len(s)
        @cache
        def recursion(index,flag):
            if index>=N: return 0
            if flag: return 1+recursion(index+1,flag) if s[index]=='0' else recursion(index+1,flag)
            else: return min(1+recursion(index+1,not flag),recursion(index+1,flag)) if s[index]=='0' else min(1+recursion(index+1,flag), recursion(index+1,not flag))
        return min(recursion(0,True),recursion(0,False))