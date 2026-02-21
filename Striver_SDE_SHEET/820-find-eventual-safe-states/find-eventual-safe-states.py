class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        check = defaultdict(lambda:True)
        vis = set()
        pathvis = set()
        def dfs(node):
            vis.add(node)
            pathvis.add(node)
            for ngh in graph[node]:
                if ngh not in vis:
                    if not dfs(ngh):
                        check[node] = False
                        return False
                elif ngh in pathvis:
                    check[node] = False
                    return False
            pathvis.remove(node)
            return True
        for node in range(len(graph)):
            if node not in vis: 
                dfs(node)
        return [node for node in range(len(graph)) if check[node]]
