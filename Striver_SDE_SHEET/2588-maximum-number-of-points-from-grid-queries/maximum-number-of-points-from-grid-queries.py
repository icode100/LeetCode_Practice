class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        N,M = len(grid),len(grid[0])
        heap = [(grid[0][0],0,0)]
        vis = {(0,0)}
        count = 0
        ans = defaultdict(int)
        for q in sorted(queries):
            while heap and heap[0][0]<q:
                val,r,c = heappop(heap)
                count+=1
                for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<N and 0<=nc<M and (nr,nc) not in vis:
                        heappush(heap,(grid[nr][nc],nr,nc))
                        vis.add((nr,nc))
            ans[q] = count
        return [ans[q] for q in queries]