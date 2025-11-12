class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        rev = defaultdict(list)
        indegree = [0]*V
        ans = list()
        for u in range(V):
            for v in graph[u]:
                rev[v].append(u)
                indegree[u]+=1
        q = deque()
        for v in range(V):
            if indegree[v]==0: q.append(v)
        while q:
            node = q.popleft()
            ans.append(node)
            for ngh in rev[node]:
                indegree[ngh]-=1
                if indegree[ngh]==0: q.append(ngh)
        return sorted(ans)
