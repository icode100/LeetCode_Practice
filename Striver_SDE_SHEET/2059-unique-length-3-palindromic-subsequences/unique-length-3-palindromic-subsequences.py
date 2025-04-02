class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left,right = {},{}
        for i,c in enumerate(s):
            if c not in left: left[c] = i
            right[c] = i
        ans = 0
        for c in set(list(s)):
            ans+=len(set(list(s[left[c]+1:right[c]])))
        return ans

        