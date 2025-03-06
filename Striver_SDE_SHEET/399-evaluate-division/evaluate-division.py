class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            [u,v],w = equations[i],values[i]
            graph[u].append((v,w))
            graph[v].append((u,1/w))
        def dfs(node,dest,current,vis):
            if node==dest: return (True,current)
            vis.add(node)
            for ngh,weight in graph[node]:
                if ngh not in vis:
                    check,ans = dfs(ngh,dest,current*weight,vis)
                    if check: return (check,ans)
            return (False,-1)
        return [dfs(u,v,1,set())[1] if u in graph and v in graph else -1 for u,v in queries]