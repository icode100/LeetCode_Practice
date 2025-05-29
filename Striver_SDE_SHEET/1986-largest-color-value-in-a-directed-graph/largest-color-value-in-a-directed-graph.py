INT_MAX = sys.maxsize
INT_MIN = -INT_MAX-1
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges: graph[u].append(v)
        vis,path = set(),set()

        def dfs(node)->int:
            if node in path: return INT_MAX
            if node in vis: return 0
            vis.add(node)
            path.add(node)
            col = colors[node]
            dp[node][col] = 1
            for ngh in graph[node]:
                if dfs(ngh)==INT_MAX: return INT_MAX
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    dp[node][c] = max(dp[node][c], dp[ngh][c]+(1 if (c==col) else 0))
            path.remove(node)
            return max(dp[node].values())
        N,res = len(colors),0
        dp = [{i:0 for i in 'abcdefghijklmnopqrstuvwxyz'} for _ in range(N)] # dp[i][j] maximum frequency of color j on any path starting from node i
        # print(dp)
        for i in range(N):
            res = max(dfs(i), res)
        return res if res!=INT_MAX else -1
        

        