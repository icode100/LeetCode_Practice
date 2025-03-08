class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top = [0]+list(accumulate(grid[0]))
        bottom = [0]+list(accumulate(grid[1]))
        print(top,bottom)
        ans = inf
        for i in range(1,len(grid[0])+1):
            ans = min(ans,max(top[-1]-top[i],bottom[i-1]))
        return ans