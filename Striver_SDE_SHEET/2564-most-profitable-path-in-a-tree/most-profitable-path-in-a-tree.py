class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        tree = defaultdict(list)
        root = 0
        
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        vis = set()
        timer = {}  
        # find bob's path
        def dfs_bob(node, parent, depth) -> bool:
            vis.add(node)
            timer[node] = depth
            if node == root: return True
            for ngh in tree[node]:
                if ngh == parent: continue
                if dfs_bob(ngh, node, depth + 1): return True
            timer.pop(node)
            return False

        dfs_bob(bob, -1,0)
        print(timer)
        vis.clear()
        ans = -100000
        # final dfs
        def dfs(node, parent, depth, current):
            nonlocal ans
            if node not in timer or depth<timer[node]: current+=amount[node]
            elif depth==timer[node]: current+=(amount[node]//2)
            if len(tree[node])==1 and node!=0: 
                ans = max(ans,current)
                return
            for ngh in tree[node]:
                if ngh != parent: dfs(ngh,node,depth+1,current)
        dfs(0,-1,0,0)
        return ans
