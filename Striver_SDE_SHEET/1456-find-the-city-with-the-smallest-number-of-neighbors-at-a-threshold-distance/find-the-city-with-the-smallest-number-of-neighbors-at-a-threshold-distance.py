class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        cost = defaultdict(lambda: defaultdict(lambda:inf))
        for i in range(n):cost[i][i] = 0
        for u,v,wt in edges:
            cost[u][v] = wt
            cost[v][u] = wt
        result = defaultdict(set)
        ans = inf
        res = -1
        for via in range(n):
            for u in range(n):
                for v in range(n):
                    cost[u][v] = min(cost[u][v],cost[u][via]+cost[via][v])
                    if cost[u][v]<=threshold and v!=u:
                        result[u].add(v)
                        
        # print(cost)

        for i in range(n):
            if len(result[i])<=ans:
                ans = len(result[i])
                res = i
        return res    
        
            