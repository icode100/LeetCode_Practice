class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vis,pathvis = set(),set()
        check = defaultdict(lambda: True)
        def dfs(node):
            vis.add(node)
            pathvis.add(node)
            for ngh in graph[node]:
                if ngh not in vis:
                    if not dfs(ngh):
                        print(node)
                        check[node] = False
                        return False
                elif ngh in pathvis:
                    check[node] = False
                    return False
            pathvis.remove(node)
            return True
        for u in range(len(graph)):
            if u not in vis: dfs(u)
            else: vis.add(u)
        # print(dict(check))
        return [u for u in range(len(graph)) if check[u]==True]
