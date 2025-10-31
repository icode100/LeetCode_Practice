class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
        stack = list()
        vis = set()
        pathvis = set()
        def dfs(node):
            vis.add(node)
            pathvis.add(node)
            for ngh in graph[node]:
                if ngh not in vis: 
                    if not dfs(ngh): return False
                elif ngh in pathvis: return False
            pathvis.remove(node)
            stack.append(node)
            return True
        for i in range(numCourses):
            if i not in vis: 
                if not dfs(i): return []
        return stack[::-1]