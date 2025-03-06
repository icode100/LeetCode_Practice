class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        heap = list()
        revgraph = defaultdict(list)
        for u,v,w in edges:
            revgraph[v].append((u,w))
        heap.append((0,0,-1))
        ans = 0
        vis = set()
        while heap:
            weight,node,parent = heappop(heap)
            if node in vis: continue
            vis.add(node)
            ans = max(ans,weight)
            for ngh,wt in revgraph[node]:
                if ngh not in vis:
                    heappush(heap,(wt,ngh,node))
        return ans if len(vis)==n else -1
        
            
