class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashset = defaultdict(int)
        ans,l = 0,0
        for r,c in enumerate(s):
            hashset[c]+=1
            while l<r and (r-l+1)-max(hashset.values())>k:
                hashset[s[l]]-=1
                l+=1
            ans = max(ans,r-l+1)
        return ans