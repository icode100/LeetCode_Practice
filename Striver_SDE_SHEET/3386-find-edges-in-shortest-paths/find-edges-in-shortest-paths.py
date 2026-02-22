class Solution:
    def findAnswer(self, N: int, edges: List[List[int]]) -> List[bool]:
        def dijkstra(graph,start):
            parent = [i for i in range(N)]
            dis = [inf for _ in range(N)]
            dis[start] = 0
            mapper = defaultdict(list)
            heap = [(0,start)]
            while heap:
                d,node = heappop(heap)
                if d > dis[node]:  
                    continue
                for ngh,wt in graph[node]:
                    if dis[ngh]>dis[node]+wt:
                        dis[ngh] = dis[node]+wt
                        heappush(heap,(dis[ngh],ngh))
                        mapper[ngh] = [node]
                    elif dis[ngh]==dis[node]+wt:
                        mapper[ngh].append(node)
            return dis
        graph = defaultdict(list)
        edgeset = set()
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
           
        dis1,dis2 = dijkstra(graph,0),dijkstra(graph,N-1)
        dest = dis1[N-1]
        if dest==inf:
            return [False]*len(edges)
        ans = list()
        for u,v,w in edges:
            if dis1[u]+w+dis2[v]==dest or dis1[v]+w+dis2[u]==dest: ans.append(True)
            else: ans.append(False)
        return ans
        




