class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w*2))
        
        heap = list()
        distance = [inf]*n
        distance[0] = 0
        heappush(heap,(0,0))

        while heap:
            dis,node = heappop(heap)
            for ngh,wt in graph[node]:
                if dis+wt<distance[ngh]:
                    distance[ngh] = dis+wt
                    heappush(heap,(distance[ngh],ngh))
        
        return distance[n-1] if distance[n-1]!=inf else -1


