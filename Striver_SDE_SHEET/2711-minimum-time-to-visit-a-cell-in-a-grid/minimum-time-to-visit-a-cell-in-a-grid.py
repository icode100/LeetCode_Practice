class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        N,M = len(grid),len(grid[0])
        if grid[0][1]>1 and grid[1][0]>1: return -1
        heap = [(0,0,0)]
        vis = {0}
        while heap:
            time,r,c = heappop(heap)
            if (r,c)==(N-1,M-1): return time
            for nr,nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0<=nr<N and 0<=nc<M and (nr,nc) not in vis:
                    if time>=grid[nr][nc]: heappush(heap,(time+1,nr,nc))
                    elif (grid[nr][nc]-time)&1: heappush(heap,(grid[nr][nc],nr,nc))
                    else: heappush(heap,(grid[nr][nc]+1,nr,nc))
                    vis.add((nr,nc))
        return -1