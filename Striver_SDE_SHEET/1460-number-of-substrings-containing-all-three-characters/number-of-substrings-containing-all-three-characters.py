class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        hashmap,ans,l = {},0,0
        for r in range(n):
            hashmap[s[r]] = hashmap.get(s[r],0)+1
            while l<r and len(hashmap)==3:
                ans+=n-r
                hashmap[s[l]]-=1
                if hashmap[s[l]]==0: hashmap.pop(s[l])
                l+=1
        return ans