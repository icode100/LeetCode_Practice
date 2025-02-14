class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # locate = defaultdict(int)
        n = len(favorite)
        global_visit = set()
        def reverse(graph):
            revgraph = defaultdict(list)
            for s,e in enumerate(graph): revgraph[e].append(s)
            return revgraph
        def longest_path(graph_dash:dict[int,list[int]],node,other):
            if node not in graph_dash: return 1
            ans = 0
            for ngh in graph_dash[node]: 
                if ngh != other: ans = max(ans,longest_path(graph_dash,ngh,other))
            return ans+1
        def cycle_len(graph:list[int],node:int,depth:int,locate:dict[int,int]):
            locate[node] = depth
            if graph[node] in locate: return [depth-locate[graph[node]]+1,node,graph[node]]
            else: return cycle_len(graph,graph[node],depth+1,locate)
        def add_to_global(graph,node):
            global_visit.add(node)
            for ngh in graph[node]:
                if ngh not in global_visit: add_to_global(graph,ngh)
        max_cycle = 0
        two_cycle = 0
        graph_dash = reverse(favorite)
        for i in range(n):
            if i not in global_visit:
                length,first,second = cycle_len(favorite,i,0,defaultdict(int))
                max_cycle = max(max_cycle,length)
                if length==2: two_cycle+=(longest_path(graph_dash,first,second)+longest_path(graph_dash,second,first))
                add_to_global(graph_dash,second)
        return max(max_cycle,two_cycle)
            

        