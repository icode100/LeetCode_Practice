class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        rev = defaultdict(list)
        for u,v,w in edges:
            rev[v].append((u,w))
        heap = [(0,0)]
        vis = set()
        ans = 0
        while heap:
            wt,node = heappop(heap)
            if node in vis: continue
            vis.add(node)
            ans = max(ans,wt)
            for ngh,wt in rev[node]:
                if ngh not in vis:
                    heappush(heap,(wt,ngh))
        return ans if len(vis)==n else -1
