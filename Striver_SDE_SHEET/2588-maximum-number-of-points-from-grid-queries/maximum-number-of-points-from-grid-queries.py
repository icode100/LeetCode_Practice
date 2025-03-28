from heapq import heappop, heappush
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        k = len(queries)
        
        heap = [(grid[0][0], 0, 0)]  
        qr = sorted((num, i) for i, num in enumerate(queries))  
        ans = [0] * k
        vis = {(0, 0)}
        
        current = 0  
        
        for q, i in qr:
            while heap and heap[0][0] < q:
                node, r, c = heappop(heap)
                current += 1
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in vis:
                        heappush(heap, (grid[nr][nc], nr, nc))  
                        vis.add((nr, nc))
            ans[i] = current
        
        return ans

                

