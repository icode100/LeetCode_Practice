class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for integer in range(low,high+1):
            s = str(integer)
            if len(s)&1==0:
                sum = 0
                for i in range(len(s)):
                    if i<(len(s)>>1): sum+=int(s[i])
                    else: sum-=int(s[i])
                ans+=int(sum==0)
        return ans
