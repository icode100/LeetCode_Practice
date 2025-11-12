class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target: return 0
        N = len(routes)
        graph = defaultdict(list)
        for bus in range(N):
            for route in routes[bus]:
                graph[route].append(bus)
        q = deque([(bus,1) for bus in graph[source]])
        mask = 0
        for bus in graph[source]: mask|=(1<<bus)
        while q:
            bus,count = q.popleft()
            for route in routes[bus]:
                if route==target: return count
                for ngh in graph[route]:
                    if (1<<ngh) & mask == 0: 
                        mask|=(1<<ngh)
                        q.append((ngh,count+1))
        return -1
