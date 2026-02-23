from typing import List

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        # DSU template
        def make_dsu():
            parent = list(range(n + 1))
            size = [1] * (n + 1)
            
            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
            
            def union(a, b):
                ra, rb = find(a), find(b)
                if ra == rb:
                    return False
                if size[ra] < size[rb]:
                    parent[ra] = rb
                    size[rb] += size[ra]
                else:
                    parent[rb] = ra
                    size[ra] += size[rb]
                return True
            
            return find, union
        
        # Two DSUs
        findA, unionA = make_dsu()
        findB, unionB = make_dsu()
        
        used_edges = 0
        
        # 1️⃣ Use type 3 first
        for t, u, v in edges:
            if t == 3:
                usedA = unionA(u, v)
                usedB = unionB(u, v)
                if usedA or usedB:
                    used_edges += 1
        
        # 2️⃣ Type 1 (Alice)
        for t, u, v in edges:
            if t == 1:
                if unionA(u, v):
                    used_edges += 1
        
        # 3️⃣ Type 2 (Bob)
        for t, u, v in edges:
            if t == 2:
                if unionB(u, v):
                    used_edges += 1
        
        # Check connectivity
        rootA = findA(1)
        rootB = findB(1)
        
        for i in range(2, n + 1):
            if findA(i) != rootA or findB(i) != rootB:
                return -1
        
        return len(edges) - used_edges