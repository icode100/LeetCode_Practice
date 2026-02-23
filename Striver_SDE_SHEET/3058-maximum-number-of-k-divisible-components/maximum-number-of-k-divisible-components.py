class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = defaultdict(list)
        for u,v in edges:
            tree[u].append(v)
            tree[v].append(u)
        self.count = 0
        def dfs(node,parent):
            current = 0
            for ngh in tree[node]:
                if ngh == parent: continue
                current+=dfs(ngh,node)
            if ((current+values[node])%k)==0:
                self.count+=1
                return 0
            return current+values[node]
        dfs(0,-1)
        return self.count