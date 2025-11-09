class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        zeros = [(i,j) for i in range(3) for j in range(3) if grid[i][j]==0]
        extras = [(i,j) for i in range(3) for j in range(3) if grid[i][j]>1]
        self.ans = int(1e9)
        def rec(i,dis):
            if i==len(zeros):
                self.ans = min(self.ans,dis)
                return 
            r,c = zeros[i]
            for nr,nc in extras:
                if grid[nr][nc]>1:
                    grid[nr][nc]-=1
                    rec(i+1,dis+abs(r-nr)+abs(c-nc))
                    grid[nr][nc]+=1
        rec(0,0)
        return self.ans