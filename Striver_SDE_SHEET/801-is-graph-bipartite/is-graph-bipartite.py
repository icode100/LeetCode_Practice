class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        vis = defaultdict(int)
        N = len(graph)
        
        def check(node):
            q = deque([node])
            while q:
                k = len(q)
                for _ in range(k):
                    node = q.popleft()
                    for ngh in graph[node]:
                        if ngh not in vis:
                            vis[ngh]=1-vis[node]
                            q.append(ngh)
                        elif vis[ngh]==vis[node]: return False
            return True
            
        for u in range(N):
            if u not in vis:
                vis[u] = 0
                if check(u)==False: return False
        return True
