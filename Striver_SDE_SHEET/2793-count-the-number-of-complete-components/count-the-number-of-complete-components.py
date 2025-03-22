class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        def find(u):
            while u!=parent[u]:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        def union(u,v):
            ultu,ultv = find(u),find(v)
            if ultu==ultv: return ultu
            if rank[ultu]<rank[ultv]:
                rank[ultv]+=rank[ultu]
                parent[ultu] = ultv
                return ultv,ultu
            else:
                rank[ultu]+=rank[ultv]
                parent[ultv] = ultu
                return ultu,ultv
        edge = defaultdict(int)
        for u,v in edges:
            if find(u)==find(v):
                edge[union(u,v)]+=1
            else:
                p,c = union(u,v)
                edge[p] += (edge[c]+1) 
        count = 0
        # print(parent,rank)
        nc2 = lambda x: (x*(x-1))//2
        p = {find(i) for i in range(n)}
        for node in p:
            # print(node,edge[node],rank[node])
            if edge[node]==nc2(rank[node]): count+=1
        return count
        