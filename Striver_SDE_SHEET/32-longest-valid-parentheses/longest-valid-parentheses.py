class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l,r,ans = 0,0,0
        for c in s:
            if c=='(': l+=1
            else: r+=1
            if l==r: ans = max(ans,r*2)
            if r>l: r=l=0
        l=r=0
        for c in s[::-1]:
            if c=='(': l+=1
            else: r+=1
            if l==r: ans = max(ans,r*2)
            if l>r: l=r=0
        return ans