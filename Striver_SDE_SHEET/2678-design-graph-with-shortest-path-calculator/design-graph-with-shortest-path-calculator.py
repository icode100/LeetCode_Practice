class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.N = n
        self.graph = defaultdict(list)
        for u,v,w in edges:
            self.graph[u].append((v,w))
        

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1],edge[2]))
        

    def shortestPath(self, i: int, j: int) -> int:
        dis = [inf for _ in range(self.N)]
        heap = list([(0,i)])
        dis[i] = 0
        while heap:
            d,node = heappop(heap)
            if d >dis[node]: continue
            for ngh,w in self.graph[node]:
                if dis[ngh]>d+w:
                    dis[ngh] = d+w
                    heappush(heap,(dis[ngh],ngh))
        return dis[j] if dis[j]!=inf else -1
        
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)