class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        dp = [0]*n
        graph = [list() for _ in range(n)]
        distance = [0]*n
        for u,v in edges:
            graph[u].append((v,0))
            graph[v].append((u,1))
        self.total = 0
        def recursion(root,depth, parent):
            distance[root] = depth
            for ngh,wt in graph[root]:
                if ngh != parent:
                    self.total+=wt
                    dp[ngh]+=dp[root]+wt
                    recursion(ngh,depth+1,root)
        recursion(0,0, -1)
        return [distance[i]+self.total-2*dp[i] for i in range(n)]


