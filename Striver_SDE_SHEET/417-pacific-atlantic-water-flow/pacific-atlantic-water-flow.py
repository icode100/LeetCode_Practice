class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        altantic = [[False] * n for _ in range(m)]
        ans = list()
        for i in range(m):
            self.dfs(heights, pacific, i, 0, -sys.maxsize-1)
            self.dfs(heights, altantic, i, n-1, -sys.maxsize-1)
        for j in range(n):
            self.dfs(heights, pacific, 0, j, -sys.maxsize-1)
            self.dfs(heights, altantic, m-1, j, -sys.maxsize-1)
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and altantic[i][j]:
                    ans.append([i, j])
        return ans
        
    def dfs(self, heights: List[List[int]], dp: List[List[bool]], i: int, j: int, pre: int) -> None:
        m, n = len(heights), len(heights[0])
        if (i < 0 or j < 0 or i >= m or j >= n or dp[i][j] or heights[i][j] < pre):
            return
        dp[i][j] = True
        self.dfs(heights, dp, i-1, j, heights[i][j])
        self.dfs(heights, dp, i+1, j, heights[i][j])
        self.dfs(heights, dp, i, j-1, heights[i][j])
        self.dfs(heights, dp, i, j+1, heights[i][j])

    