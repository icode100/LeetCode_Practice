class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        maxi = [[0 for _ in range(n)] for __ in range(n)]
        for i in range(n):
            for j in range(i,n):
                if j==i: maxi[i][j] = arr[i]
                else:
                    maxi[i][j] = max(maxi[i][j-1],arr[j])
        @cache
        def recursion(i,j):
            if i==j: return 0
            ans = sys.maxsize
            for k in range(i,j): ans = min(ans,maxi[i][k]*maxi[k+1][j]+recursion(i,k)+recursion(k+1,j))
            return ans
        return recursion(0,n-1)


        

