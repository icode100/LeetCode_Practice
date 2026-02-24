class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        N = len(fruits)
        limit = ceil(N/2)
        @cache
        def recursion_child3(r,c):
            if r==N-1 and c==N-1:
                return 0
            ans = 0
            for nr,nc in [(r-1,c+1),(r,c+1),(r+1,c+1)]:
                if nr>=N or nc>=N or nc<0 or nr<0: continue
                if (nr==N-1 and nc<=nr) or (nr>=limit and nc<nr):
                    ans = max(ans,recursion_child3(nr,nc))
            return ans+fruits[r][c]
        @cache
        def recursion_child2(r,c):
            if r==N-1 and c==N-1: return 0
            ans = 0
            for nr,nc in [(r+1,c-1),(r+1,c),(r+1,c+1)]:
                if nr>=N or nc>=N or nc<0 or nr<0: continue
                if (nc==N-1 and nc>=nr) or (nc>=limit and nc>nr):
                    ans = max(ans,recursion_child2(nr,nc))
            return ans+fruits[r][c]
        ans = 0
        for i in range(N):
            ans+=fruits[i][i]
        return ans+recursion_child2(0,N-1)+recursion_child3(N-1,0)

