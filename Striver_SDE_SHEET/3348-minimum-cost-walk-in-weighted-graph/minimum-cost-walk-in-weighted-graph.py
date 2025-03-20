class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        value = [((1<<64)-1) for _ in range(n)]
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        def union(u,v,w):
            ultu,ultv = find(u),find(v)
            if ultu==ultv: 
                value[ultu]&=w
                return False
            if rank[ultu]>rank[ultv]:
                parent[ultv] = ultu
                rank[ultu]+=rank[ultv]
                value[ultu] = value[ultu]&value[ultv]&w
            else:
                parent[ultu] = ultv
                rank[ultv]+=rank[ultu]
                value[ultv] = value[ultu]&value[ultv]&w
            return True
        for u,v,w in edges:
            union(u,v,w)
        print(value)
        ans = list()
        for s,d in query:
            if find(s)!=find(d): ans.append(-1)
            else:
                ans.append(value[find(s)])
        return ans

        


