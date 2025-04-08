class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N = len(s)
        M = len(p)
        freq = Counter(p)
        check = Counter(s[:M])
        l = 0
        ans = list()
        for r in range(M,N):
            if check==freq: ans.append(l)
            check[s[r]]+=1
            check[s[l]]-=1
            if check[s[l]]==0: check.pop(s[l])
            l+=1
        if check==freq: ans.append(l)
        return ans
        
            
