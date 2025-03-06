class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            [u,v],w = equations[i],values[i]
            graph[u].append((v,w))
            graph[v].append((u,1/w))
        def dfs(node,dest,current,vis):
            if node==dest: return current
            vis.add(node)
            for ngh,weight in graph[node]:
                if ngh not in vis:
                    ans = dfs(ngh,dest,current*weight,vis)
                    if ans!=-1: return ans
            return -1
        return [dfs(u,v,1,set()) if u in graph and v in graph else -1 for u,v in queries]