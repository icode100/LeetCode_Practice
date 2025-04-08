class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        counter = {}
        l = 0
        ans = 0
        for r in range(N):
            counter[s[r]] = counter.get(s[r], 0)+1
            while l<r and counter and (r-l+1-max(counter.values()))>k:
                counter[s[l]]-=1
                l+=1
            ans = max(ans,r-l+1)
        ans = max(ans,r-l+1)
        return ans
