class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def recursion(i,j):
            if i+2>j: return 0
            if i+2==j: return values[i]*values[i+1]*values[i+2]
            ans = sys.maxsize
            for k in range(i+1,j):
                part1 = values[i]*values[k]*values[j]
                part2 = recursion(i,k)
                part3 = recursion(k,j)
                ans = min(ans,part1+part2+part3)
            return ans
        N = len(values)
        return recursion(0,N-1)

