class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1: return s
        if len(s)==2 and s==s[1]: return s
        maxlen,ans = 0,""
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > maxlen:
                    ans = s[l:r+1]
                    maxlen = r-l+1
                l-=1
                r+=1
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > maxlen:
                    ans = s[l:r+1]
                    maxlen = r-l+1
                l-=1
                r+=1
        return ans
