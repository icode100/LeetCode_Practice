class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = set(arr)
        mod = int(1e9+7)
        @cache
        def recursion(root):
            total = 1
            for i in arr:
                if root%i==0 and root//i in arr: total = (total+recursion(i)*recursion(root//i))%mod
            return total%mod
        return sum([recursion(root) for root in arr])%mod
