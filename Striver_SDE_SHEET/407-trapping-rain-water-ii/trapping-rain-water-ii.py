class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        N,M = len(heightMap),len(heightMap[0])
        heap = list()
        vis = set()
        ans = 0
        for i in range(N):
            for j in range(M):
                if i==0 or j==0 or i==N-1 or j==M-1: 
                    heappush(heap,(heightMap[i][j],i,j))
                    vis.add((i,j))
        while heap:
            node,r,c = heappop(heap)
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=nr<N and 0<=nc<M and (nr,nc) not in vis:
                    if heightMap[nr][nc]<node:ans+=node-heightMap[nr][nc]
                    heappush(heap,(max(heightMap[nr][nc],node),nr,nc))
                    vis.add((nr,nc))
        return ans
