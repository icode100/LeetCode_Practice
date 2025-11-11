class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        V = len(graph)
        target = (1<<V)-1
        q = deque()
        vis = set()
        for node in range(V):
            q.append((node,1<<node,0))
            vis.add((node,1<<node))
        while q:
            node,mask,step = q.popleft()
            if mask==target: return step
            for ngh in graph[node]:
                if (ngh,mask|1<<ngh) not in vis:
                    q.append((ngh,mask|1<<ngh,step+1))
                    vis.add((ngh,mask|1<<ngh))
        return -1