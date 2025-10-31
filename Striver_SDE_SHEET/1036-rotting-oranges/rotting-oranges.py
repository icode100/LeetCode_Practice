class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N,M = len(grid),len(grid[0])
        q = deque()
        vis = set()
        for i in range(N):
            for j in range(M):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    vis.add((i,j,0))
        # print(q)
        count = 0
        while q:
            K = len(q)
            print(q)
            print(count)
            for _ in range(K):
                r,c,count = q.popleft()
                for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr,nc = r+dr,c+dc
                    if 0<=nr and nr<N and 0<=nc and nc<M and grid[nr][nc]==1 and (nr,nc) not in vis:
                        q.append((nr,nc,count+1))
                        vis.add((nr,nc))
        for i in range(N):
            for j in range(M):
                if grid[i][j]==1 and (i,j) not in vis: return -1
        return count
        
