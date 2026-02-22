class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def build(edges):
            graph = defaultdict(list)
            for u,v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def findDia(graph):
            dia = 0
            def dfs(node,parent):
                max1 = 0
                max2 = 0
                nonlocal dia
                for ngh in graph[node]:
                    if ngh==parent: continue
                    h = dfs(ngh,node)
                    if h>max1: 
                        max2 = max1
                        max1 = h
                    elif h>max2: max2 = h
                dia = max(dia,max1+max2)
                return max1+1
            dfs(0,-1)
            return dia
        
        g1,g2 = build(edges1),build(edges2)

        d1,d2 = findDia(g1),findDia(g2)

        return max(d1,d2,ceil(d1/2)+ceil(d2/2)+1)

