class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m,n = len(grid), len(grid[0])
        k = m*n 
        checkset = set()
        sumi = 0
        for i in range(m):
            for j in range(n):
                checkset.add(grid[i][j]%x)
                sumi+=grid[i][j]
        if len(checkset)>1: return -1
        nums = sorted(grid[i][j] for i in range(m) for j in range(n))
        ans = inf
        current = 0
        for i in range(k):
            ans = min(ans,(nums[i]*i - current + sumi-current-(nums[i]*(k-i)) )//x)
            current+=nums[i]
        return max(ans,0)