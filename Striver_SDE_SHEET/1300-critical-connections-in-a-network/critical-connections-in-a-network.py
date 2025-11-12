class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [list() for _ in range(n)]
        for u,v in connections: 
            graph[u].append(v)
            graph[v].append(u)
        ans = list()
        vis = set()
        tin = [0]*n
        l_tin = [0]*n
        def recursion(node,parent,time):
            vis.add(node)
            tin[node] = l_tin[node] = time
            for ngh in graph[node]:
                if ngh!=parent:
                    if ngh not in vis:
                        recursion(ngh,node,time+1)
                        l_tin[node] = min(l_tin[node],l_tin[ngh])
                        if l_tin[ngh]>tin[node]: ans.append([ngh,node])
                    else: l_tin[node] = min(l_tin[node],l_tin[ngh])
        recursion(0,-1,1)
        return ans