class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = int(1e9+7)
        graph = defaultdict(list)
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        q = list()
        q.append((0,0))
        distance = [sys.maxsize]*n
        distance[0] = 0
        path = [1]+[0]*(n-1)
        while q:
            dis,node = heappop(q)
            for ngh,wt in graph[node]:
                if dis+wt<distance[ngh]:
                    distance[ngh] = dis+wt
                    path[ngh] = path[node]
                    heappush(q,(distance[ngh],ngh))
                elif dis+wt==distance[ngh]:
                    path[ngh] = (path[node] + path[ngh])%mod
        return (path[n-1])%mod
                