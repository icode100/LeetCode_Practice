class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        heap = [(grid[0][0],0,0)]
        vis = {(0,0)}
        while heap:
            dis,r,c = heappop(heap)
            if r==N-1 and c==N-1: return dis
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=nr<N and 0<=nc<N and (nr,nc) not in vis:
                    heappush(heap,(max(grid[nr][nc],dis),nr,nc))
                    vis.add((nr,nc))
        return -1
