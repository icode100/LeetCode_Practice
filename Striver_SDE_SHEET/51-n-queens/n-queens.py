class Solution:
    def isfeasible(self,grid:List[List[int]],row:int,col:int,n:int)->bool:
        if 1 in grid[row]:
            return False
        i = row 
        j = col
        while 0<=i and 0<=j:
            if grid[i][j]==1:
                return False
            i-=1
            j-=1
        i=row
        j = col
        while i<=n-1 and j>=0:
            if grid[i][j]==1:
                return False
            i+=1
            j-=1
        return True
      


        
    def solve(self,grid,col,n,ans):
        if col==n:
            ans.append(deepcopy(grid))
            # print(ans)
            return
        for row in range(n):
            if self.isfeasible(grid,row,col,n):
                grid[row][col] = 1
                self.solve(grid,col+1,n,ans)
                grid[row][col] = 0
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [[0 for i in range(n)] for i in range(n)]
        ans = list(list(list()))
        self.solve(grid,0,n,ans)
        finans = list(list(str()))
        for i in ans:
            temp = list()
            for it in i:
                dim = str()
                for ii in it:
                    if ii==1:
                        dim+="Q"
                    else:
                        dim+="."
                temp.append(dim)
            finans.append(temp.copy())
        return finans
