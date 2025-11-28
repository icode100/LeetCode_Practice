class Solution:
    def maxKDivisibleComponents(self, N: int, edges: List[List[int]], values: List[int], k: int) -> int:

        graph = [list() for _ in range(N)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        def dfs(node,parent):
            
            current = 0
            for ngh in graph[node]:
                if ngh != parent:

                    k_comp,val = dfs(ngh,node)
                    values[node]+=val
                    current+=k_comp
            
            if values[node]%k == 0:
                current+=1
                values[node] = 0
            
            return current,values[node]
        
        return dfs(0,-1)[0]

            

            