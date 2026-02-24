class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        '''
        * for every node that does have extra edges there can be two options
            * disconnect all the extra edges from the child part
            * disconnect one edge from the parent part and the remaining from the child part
        * from the leaf node propagate these two options performing a take and not take operation and hence dp
        * also if the child have already removed the edge to parent we do not need to count it while computing for the parent
        * we sort the results we got from the children based on the gains where gain is difference between the case of removing parent edge and keeping parent edge
        '''

        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        @cache
        def dfs(node,parent):
            base = 0
            gain = list()
            for ngh,w in graph[node]:
                if ngh == parent: continue
                choseparent,notchoseparent = dfs(ngh,node)
                base+=notchoseparent
                gain.append(
                    (choseparent+w)-notchoseparent
                )
            new_choseparent = sum(nlargest(k-1,filter(lambda x: x>0, gain)))
            new_notchoseparent = sum(nlargest(k,filter(lambda x: x>0, gain)))
            return new_choseparent+base, new_notchoseparent+base
        return dfs(0,-1)[1]
            

