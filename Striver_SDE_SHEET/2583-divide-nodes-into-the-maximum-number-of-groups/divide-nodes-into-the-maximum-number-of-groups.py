from collections import defaultdict, deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        color = {}  

        def check(root):
            color[root] = 0
            q = deque([root])
            components = []
            while q: 
                node = q.popleft()
                components.append(node)
                for ngh in graph[node]:
                    if ngh not in color:
                        color[ngh] = 1 - color[node]
                        q.append(ngh)
                    elif color[ngh] == color[node]: 
                        return [], False  
            return components, True

        def find_groups(root):
            vis = set([root])
            dq = deque([(root, 1)])
            max_depth = 1
            while dq:
                for _ in range(len(dq)):
                    node, depth = dq.popleft()
                    max_depth = max(max_depth, depth)
                    for ngh in graph[node]:
                        if ngh not in vis: 
                            dq.append((ngh, depth + 1))
                            vis.add(ngh)
            return max_depth

        res = 0
        for i in range(1, n + 1):
            if i not in color:
                comp, is_bipartite = check(i)
                if not is_bipartite: 
                    return -1
                max_group_size = 0
                for node in comp:
                    max_group_size = max(max_group_size, find_groups(node))
                res += max_group_size
        
        return res
