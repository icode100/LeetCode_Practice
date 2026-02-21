class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        @cache
        def recursion(i,j):
            if j<i+2: return 0
            if i+2==j: return values[i]*values[i+1]*values[i+2]
            return min(
                values[i]*values[j]*values[k] + recursion(i,k) + recursion(k,j)
                for k in range(i+1,j)
            )
        return recursion(0,len(values)-1)