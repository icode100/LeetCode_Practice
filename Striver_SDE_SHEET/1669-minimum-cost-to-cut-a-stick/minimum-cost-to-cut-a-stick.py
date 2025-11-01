class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        @cache
        def recursion(i,j):
            if i>j: return 0
            return min([cuts[j+1]-cuts[i-1]+recursion(i,k-1)+recursion(k+1,j) for k in range(i,j+1)])
        return recursion(1,len(cuts)-2)
