class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        @cache
        def recursion(index):
            if index==N: return 0
            maxi = 0
            ans = 0
            for i in range(index,min(index+k,N)):
                maxi = max(arr[i],maxi)
                ans = max(ans,(i-index+1)*maxi+recursion(i+1))
            return ans
        return recursion(0)

