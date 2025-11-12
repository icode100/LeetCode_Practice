class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        N,M = len(heights),len(heights[0])
        def recursion(r,c,vis):
            vis.add((r,c))
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=nr<N and 0<=nc<M and (nr,nc) not in vis and heights[nr][nc]>=heights[r][c]:
                    recursion(nr,nc,vis)
        p = set()
        a = set()
        for i in range(N):
            for j in range(M):
                if i==0 or j==0: recursion(i,j,p)
                if i==N-1 or j==M-1: recursion(i,j,a)
        return list(a&p)