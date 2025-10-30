class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target: return 0
        N = len(routes)
        graph = defaultdict(list)
        for bus in range(N):
            for stop in routes[bus]:
                graph[stop].append(bus)
        q = deque()
        vis = set()
        for bus in graph[source]:
            q.append(bus)
            vis.add(bus)
        count = 1
        while q:
            K = len(q)
            for _ in range(K):
                bus = q.popleft()
                for next in routes[bus]:
                    if next==target: return count
                    for nextbus in graph[next]:
                        if nextbus not in vis:
                            vis.add(nextbus)
                            q.append(nextbus)
            count+=1
        return -1
        