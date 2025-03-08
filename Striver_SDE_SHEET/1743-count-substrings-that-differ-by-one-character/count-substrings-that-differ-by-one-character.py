class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i]!=t[j]:
                    left = 1
                    while i-left>=0 and j-left>=0 and s[i-left]==t[j-left]:
                        left+=1
                    right = 1
                    while right+i<len(s) and right+j<len(t) and s[i+right]==t[j+right]:
                        right+=1
                    ans+=left*right
        return ans


