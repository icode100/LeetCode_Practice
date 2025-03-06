class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s,d,di in flights:
            graph[s].append((d,di))
        q = deque([(0,0,src)])
        distance = [inf]*n
        distance[src] = 0
        while q:
            step,dis,node = q.popleft()
            if step>k: continue
            for it,wt in graph[node]:
                if distance[it]>dis+wt and step<=k:
                    distance[it] = dis+wt
                    q.append((step+1,dis+wt,it))
        return distance[dst] if distance[dst]!=inf else -1