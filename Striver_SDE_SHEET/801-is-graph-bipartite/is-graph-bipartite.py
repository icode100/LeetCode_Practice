class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        vis = defaultdict(int)
        N = len(graph)
        
        def dfs(node,col):
            vis[node] = col
            for ngh in graph[node]:
                if ngh not in vis: 
                    if dfs(ngh,1-col)==False: return False
                elif vis[ngh] == col: return False
            return True
            
        for u in range(N):
            if u not in vis:
                if dfs(u,0)==False: return False
        return True
