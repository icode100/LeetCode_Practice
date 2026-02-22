class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        N = len(edges1)+1
        for u,v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
        for u,v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        def build(graph):
            count = [0,0]
            q = deque([(0,-1,0)])
            color = defaultdict(int)
            while q:
                node,parent,c = q.popleft()
                color[node] = c
                count[c]+=1
                for ngh in graph[node]:
                    if ngh != parent:
                        q.append((ngh,node,1-c))
            return count,color
        
        count1,color1 = build(graph1)
        count2,color2 = build(graph2)
        ans = list()
        for i in range(N):
            col = color1[i]
            ans.append(count1[col]+max(count2))
        return ans
            




