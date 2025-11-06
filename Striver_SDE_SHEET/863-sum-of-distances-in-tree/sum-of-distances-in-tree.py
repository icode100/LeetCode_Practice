class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dp = [0]*n
        children=[1]*n
        def recursion(node,parent):
            for ngh in graph[node]:
                if ngh != parent:
                    recursion(ngh,node)
                    children[node]+=children[ngh]
                    dp[node]+=dp[ngh]+children[ngh]
        recursion(0,-1) 
        def recursion2(node,parent):
            for ngh in graph[node]:
                if ngh != parent:
                    dp[ngh] = (dp[node]-children[ngh]) + (n-children[ngh])
                    recursion2(ngh,node)
        recursion2(0,-1)
        return dp
                    



            
