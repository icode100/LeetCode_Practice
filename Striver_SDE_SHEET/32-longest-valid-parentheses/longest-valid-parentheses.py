class Solution:
    def longestValidParentheses(self, s):
        # dp[i] = Longest valid parantheses till index i
        if s=='': return 0
        dp = [0]*len(s)
        for i,c in enumerate(s):
            if c==')':
                if i>0 and s[i-1]=='(': 
                    dp[i] =(dp[i-2]+2) if i-2>0 else 2
                elif i-dp[i-1]>0 and s[i-dp[i-1]-1]=='(': 
                    dp[i] =(dp[i-1]+dp[i-dp[i-1]-2]+2) if i-dp[i-1]-2>=0 else (dp[i-1]+2)
        print(dp)
        return max(dp)