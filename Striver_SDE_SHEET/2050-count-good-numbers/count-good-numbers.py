class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = (n>>1)+1 if n&1 else (n>>1)
        odd = n-even
        mod = int(1e9+7)
        return (((pow(5,even,mod))%mod )*(pow(4,odd, mod))) % mod