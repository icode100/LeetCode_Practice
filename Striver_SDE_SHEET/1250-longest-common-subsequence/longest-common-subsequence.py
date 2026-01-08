class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1,N2 = len(text1),len(text2)
        
        @cache
        def recursion(i,j):
            if i>=N1 or j>=N2: return 0

            notpick = max(recursion(i,j+1),recursion(i+1,j))
            pick = 0
            if text1[i]==text2[j]: pick = 1+recursion(i+1,j+1)

            return max(pick,notpick)
        
        return recursion(0,0)