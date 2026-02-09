class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        '''
        * so if we can know that whether a subtree at a branch does have apples or not then we can easily prune the branches 
        * for that may be we can do a dfs just to maintain a hashmap with boolean value and key being the root node in the subtree
        * 
        '''
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        hashmap = [False]*n
        def dfs1(root,parent):
            for ngh in graph[root]:
                if ngh != parent:
                    if dfs1(ngh,root):
                        hashmap[root] = True
                    if hasApple[ngh] == True:
                        hashmap[root] = True
    
            return hashmap[root]            
        dfs1(0,-1)
        print(hashmap)
        count = 0
        def dfs2(root,parent):
            nonlocal count
            for ngh in graph[root]:
                if ngh != parent:
                    if hashmap[ngh]:
                        count+=2
                        dfs2(ngh,root)
                    elif hasApple[ngh]:
                        count+=2
        dfs2(0,-1)
        return count



                
