from collections import deque
from typing import List

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        visited = set()
        
        q = deque()
        q.append((0, 0, True)) 
        visited.add((0, True))
        limit = max(x, max(forbidden, default=0)) + a + b + 1000
        while q:
            node, step, can_back = q.popleft()
            if node == x:
                return step
            f = node + a
            if f <= limit and f not in forbidden and (f, True) not in visited:
                visited.add((f, True))
                q.append((f, step + 1, True))
            if can_back:
                bck = node - b
                if bck >= 0 and bck not in forbidden and (bck, False) not in visited:
                    visited.add((bck, False))
                    q.append((bck, step + 1, False))
        
        return -1