class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = [0]*(n+1)
        hashset = set()
        def recursion(i,last):
            if i==n+1: return True
            if pattern[i-1]=='I':
                for k in range(last+1,10):
                    if k in hashset: continue
                    ans[i] = k
                    hashset.add(k)
                    if recursion(i+1,k): return True
                    ans[i] = 0
                    hashset.remove(k)
            else:
                for k in range(1,last):
                    if k in hashset: continue
                    ans[i] = k
                    hashset.add(k)
                    if recursion(i+1,k): return True
                    ans[i] = 0
                    hashset.remove(k)
            return False
        i = 0
        while i<n and pattern[i]!='I': i+=1
        hashset.add(i+1)
        ans[0] = i+1
        recursion(1,i+1)
        string = ""
        for i in ans: string+=str(i)
        return string

