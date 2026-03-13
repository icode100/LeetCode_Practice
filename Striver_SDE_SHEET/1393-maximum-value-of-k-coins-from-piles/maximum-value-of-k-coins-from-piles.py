class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        N = len(piles)
        for i,pile in enumerate(piles):
            K = len(pile)
            for j in range(1,K):
                piles[i][j] += piles[i][j-1]
        @cache
        def dfs(i,rem):
            if i==N: return 0
            ans = 0
            for j in range(rem+1):
                idx = j-1
                if idx>=len(piles[i]): break
                ans = max(
                    ans,
                    piles[i][idx]+dfs(i+1,rem-j) if idx>=0 else dfs(i+1,rem)
                )
            return ans
        ans = dfs(0,k)
        dfs.cache_clear()
        return ans
                