from collections import defaultdict
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i: i for i in range(1, n + 1)}
        rank = {i: 0 for i in range(1, n + 1)}

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]  
                node = parent[node]
            return node

        def union(n1,n2):
            u1,u2 = find(n1),find(n2)
            if u1==u2: return False
            if rank[u1]<rank[u2]:
                parent[u1] = u2
                rank[u2]+=1
            else:
                parent[u2] = u1
                rank[u1]+=1
            return True
        for u, v in edges:
            if not union(u, v): return [u, v]

