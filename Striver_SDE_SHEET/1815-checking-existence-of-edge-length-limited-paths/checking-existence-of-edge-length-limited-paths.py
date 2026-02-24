class Solution:
    def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]
        def find(u):
            if parent[u]==u: return u
            parent[u] = find(parent[u])
            return parent[u]
        def union(u,v):
            ultu,ultv = find(u),find(v)
            if ultu==ultv: return False
            if size[ultu]<size[ultv]:
                parent[ultu] = ultv
                size[ultv]+=size[ultu]
            else:
                parent[ultv] = ultu
                size[ultu]+=size[ultv]
            return True
    
        new_queries = [(l,i,u,v) for i,(u,v,l) in enumerate(queries)]
        heapify(new_queries)
        edges = [(w,a,b) for a,b,w in edges]
        heapify(edges)
        ans = [False]*len(queries)
        while new_queries:
            l,i,u,v = heappop(new_queries)
            while edges and edges[0][0]<l:
                w,a,b = heappop(edges)
                union(a,b)
            ans[i] = (find(u)==find(v))
        return ans

        



