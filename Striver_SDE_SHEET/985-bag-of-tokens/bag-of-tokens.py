class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        score = 0
        l,r = 0,n-1
        ans = 0
        if not tokens or power<tokens[0]: return 0
        while l<r:
            while l<=r and tokens[l]<=power:
                score+=1
                power-=tokens[l]
                l+=1
                ans = max(score,ans)
                print(l,r)
            while l<=r and score>=1 and tokens[l]>power:
                score-=1
                power+=tokens[r]
                r-=1
                print(l,r)

        if l==r and l<n:
            if tokens[l]<=power:
                score+=1
                ans = max(ans,score)
        ans = max(ans,score)
        return ans
