class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        rev_row = lambda i: [1-grid[i][j] for j in range(n)]
        
        for i in range(m):
            if grid[i][0]==0: grid[i] = rev_row(i)
        # print(grid)
        for i in range(1,n):
            countz = 0
            for j in range(m):
                countz += int(grid[j][i]==0)
            if m-countz < countz:
                for j in range(m):
                    grid[j][i] = 1-grid[j][i]
        print(grid)
        ans = 0
        for i in range(m):
            num = 0
            for j in range(n):
                num = (num<<1)
                num = num|grid[i][j]
            ans+=num
        return ans