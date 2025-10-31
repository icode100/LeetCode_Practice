class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[sys.maxsize for _ in range(n)] for _ in range(n)]
        for i in range(n): distance[i][i] = 0
        for u,v,w in edges:
            distance[u][v] = w
            distance[v][u] = w
        result = defaultdict(set)
        ans = inf
        res = -1
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    distance[u][v] = min(distance[u][v],distance[u][k]+distance[k][v])
                    if distance[u][v]<=distanceThreshold and u!=v: result[u].add(v)
        for i in range(n):
            if len(result[i])<=ans:
                ans = len(result[i])
                res = i
        return res