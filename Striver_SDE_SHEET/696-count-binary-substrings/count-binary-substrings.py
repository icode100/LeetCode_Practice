class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        j = 0
        i = 0
        ans = 0
        prev = s[i]
        counts,countf = 0,0
        while j<n and s[j]==prev:
            j+=1
            countf+=1
        if j==n:
            return 0
        while j<n:
            while j<n and s[j]!=prev:
                j+=1
                counts+=1
            ans+=min(counts,countf)
            countf = counts
            counts = 0
            prev = s[j-1]
        return ans+min(countf,counts)




            