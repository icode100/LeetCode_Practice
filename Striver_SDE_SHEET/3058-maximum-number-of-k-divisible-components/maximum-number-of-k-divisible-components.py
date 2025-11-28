class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans = 0
        def recursion(node,parent):
            nonlocal ans
            ret = values[node]
            for ngh in graph[node]:
                if ngh != parent: ret+=recursion(ngh,node)
            if ret%k==0:
                ans+=1
                ret = 0
            return ret
        recursion(0,-1)
        return ans

            
