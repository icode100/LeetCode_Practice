class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        N,M = len(matrix),len(matrix[0])
        q = deque()
        vis = set()
        for i in range(N):
            for j in range(M):
                if matrix[i][j]==0:
                    q.append((i,j,0))
                    vis.add((i,j))
        while q:
            r,c,level = q.popleft()
            for nr,nc in [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]:
                if 0<=nr<N and 0<=nc<M and (nr,nc) not in vis:
                    matrix[nr][nc] = level+1
                    q.append((nr,nc,level+1))
                    vis.add((nr,nc))
        return matrix