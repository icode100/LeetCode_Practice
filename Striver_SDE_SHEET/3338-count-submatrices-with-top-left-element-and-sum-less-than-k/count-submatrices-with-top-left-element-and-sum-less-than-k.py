class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        R,C = len(grid), len(grid[0])
        if grid[0][0]>k: return 0
        count = 1
        for i in range(1,C):
            grid[0][i]+=grid[0][i-1]
            count+=int(grid[0][i]<=k)
        for i in range(1,R):
            grid[i][0]+=grid[i-1][0]
            count+=int(grid[i][0]<=k)
        
        for i in range(1,R):
            for j in range(1,C):
                grid[i][j]+=(grid[i-1][j]+grid[i][j-1]-grid[i-1][j-1])
                count+= int(grid[i][j]<=k)
        return count

