class Solution:
    def almostPalindromic(self, s: str) -> int:
        N = len(s)
        def expand(l,r):
            while l>=0 and r<N and s[l]==s[r]:
                l-=1
                r+=1
            return l,r
        maxlen = 0
        for i in range(N):

            # oddlength
            l,r = expand(i,i)
            maxlen = max(maxlen,r-l)

            l1,r1 = expand(l-1,r)
            maxlen = max(maxlen,r1-l1-1)

            l2,r2 = expand(l,r+1)
            maxlen = max(maxlen,r2-l2-1)


            # evenlength
            l,r = expand(i,i+1)
            maxlen = max(maxlen,r-l)
            
            l1,r1 = expand(l-1,r)
            maxlen = max(maxlen,r1-l1-1)

            l2,r2 = expand(l,r+1)
            maxlen = max(maxlen, r2-l2-1)
        return min(maxlen,N)




