class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        '''
        * a node cannot be part of two cycles
        * a single component cannot have more than one cycles
        * a node which is part of cycle wont have any outward node to non cyclic node
        '''
        N = len(edges)
        graph = [[] for _ in range(N)]
        indegree = [0]*N
        for u,v in enumerate(edges):
            if v==-1:
                graph[u] = []
                continue
            graph[u].append(v)
            indegree[v]+=1
        print(indegree)
        q = deque()
        for node,ind in enumerate(indegree):
            if ind==0: q.append(node)
        print(q)
        while q:
            node = q.popleft()
            for ngh in graph[node]:
                indegree[ngh]-=1
                if indegree[ngh]==0:
                    q.append(ngh)
        ans = 0
        vis = set()
        for node in range(len(edges)):
            if indegree[node]>0 and node not in vis:
                current = node
                cycle = 0
                while current not in vis:
                    vis.add(current)
                    print(current)
                    current = graph[current][0]
                    cycle+=1
                ans = max(ans,cycle)
                
        return ans if ans>0 else -1

