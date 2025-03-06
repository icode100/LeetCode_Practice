from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        coloured = [-1 for i in range(len(graph))]
        def check(node):
            q = deque()
            q.append(node)
            coloured[node]=0
            while q:
                curr = q.popleft()
                for neighbor in graph[curr]:
                    if coloured[neighbor]==-1:
                        coloured[neighbor] = int(not coloured[curr])
                        q.append(neighbor)
                    elif coloured[neighbor]==coloured[curr]:
                        return False
            return True



        for i in range(len(graph)):
            if coloured[i]==-1:
                if check(i) is False:
                    return False
        return True