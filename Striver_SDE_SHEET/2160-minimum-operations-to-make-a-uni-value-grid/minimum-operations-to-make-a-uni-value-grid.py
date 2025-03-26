class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m,n = len(grid), len(grid[0])
        k = m*n 
        nums = sorted([grid[i][j] for i in range(m) for j in range(n)])
        num = nums[k>>1]
        ans = 0
        for i in range(m):
            for j in range(n):
                if abs(grid[i][j]-num)%x!=0: return -1
                ans+=abs(grid[i][j]-num)//x
        return ans