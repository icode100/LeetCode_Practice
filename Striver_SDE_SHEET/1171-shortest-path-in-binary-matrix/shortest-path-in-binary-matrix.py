class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        distance = [[inf]*N for _ in range(N)]
        heap = [(0,0,0)]
        distance[0][0] = 1 if grid[0][0]==0 else inf
        while heap:
            dis,r,c = heappop(heap)
            # print(r,c)
            for dr,dc in list(product([-1,0,1],[-1,0,1])):
                if dr==0 and dc==0: continue
                nr,nc = r+dr,c+dc
                if 0<=nr<N and 0<=nc<N and grid[nr][nc]==0 and distance[nr][nc]>distance[r][c]+1:
                    # print('hi')
                    distance[nr][nc]=distance[r][c]+1
                    heappush(heap,(distance[nr][nc],nr,nc))
        # print(distance)
        return distance[N-1][N-1] if distance[-1][-1]!=inf else -1
