class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(list)
        for u,v in edges:
            tree[u].append(v)
            tree[v].append(u)
        ans = [0 for _ in range(n)]
        def recursion(node,parent):
            di = {labels[node]:1}
            for ngh in tree[node]:
                if ngh != parent:
                    temp = recursion(ngh,node)
                    for k,v in temp.items():
                        di[k] = di.get(k,0)+v
            ans[node] = di[labels[node]]
            return di
        recursion(0,-1)
        return ans