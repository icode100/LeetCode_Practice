class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = defaultdict(int)
        l = 0
        ans = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset[s[l]]-=1
                if hashset[s[l]]==0: hashset.pop(s[l])
                l+=1
            hashset[s[r]]+=1
            ans = max(ans,r-l+1)
        return ans