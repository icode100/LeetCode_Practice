class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        ans = 0
        l=0
        checkset = Counter()
        for r in range(N):
            checkset[s[r]]+=1
            while l<r and len(checkset)==3:
                ans+=(N-r)
                checkset[s[l]]-=1
                if checkset[s[l]]==0: checkset.pop(s[l])
                l+=1
        return ans

