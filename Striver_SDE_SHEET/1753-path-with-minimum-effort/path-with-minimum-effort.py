class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        distance = [[inf for _ in range(M)] for _ in range(N)]
        heap = [(0,0,0)]
        distance[0][0] = 0
        print(distance)
        while heap:
            dis,r,c = heappop(heap)
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                nr,nc = r+dr,c+dc
                if 0<=nr<N and 0<=nc<M and distance[nr][nc]>max(dis,abs(grid[nr][nc]-grid[r][c])):
                    distance[nr][nc]=max(dis,abs(grid[nr][nc]-grid[r][c]))
                    heappush(heap,(distance[nr][nc],nr,nc))
        return distance[-1][-1]