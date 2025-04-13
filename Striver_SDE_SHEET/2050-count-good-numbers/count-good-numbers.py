class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = int(1e9+7)
        even = ceil(n/2)
        odd = n-even
        return (((pow(5,even,mod))%mod )*(pow(4,odd, mod))) % mod