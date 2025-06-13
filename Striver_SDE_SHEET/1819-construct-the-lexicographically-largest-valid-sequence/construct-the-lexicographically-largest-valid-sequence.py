class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        N = (2*n)-1
        vis = set()
        ans = [0]*N
        def dfs(index):
            if index>=N: return True
            if ans[index]!=0: return dfs(index+1)
            for i in range(n,0,-1):
                if i not in vis:
                    ans[index] = i
                    vis.add(i)
                    if i != 1:
                        if index+i<N and ans[index+i]==0:
                            ans[index+i] = i
                            if dfs(index+1): return True
                            ans[index+i] = 0
                    else:
                        if dfs(index+1): return True
                    vis.remove(i)
                    ans[index] = 0
            return False 
        dfs(0)
        return ans


