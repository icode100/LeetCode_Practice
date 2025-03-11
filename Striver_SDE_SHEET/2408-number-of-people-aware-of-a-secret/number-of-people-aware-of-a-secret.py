class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = int(1e9+7)
        dp = [0]*forget
        dp[forget-1] = 1
        for i in range(n-1):
            temp = dp[1:]
            sumi = 0
            for j in range(forget-delay):
                sumi+=temp[j]
            temp.append(sumi%mod)
            dp[::] = temp[::]
            del temp
        return sum(dp)%mod

            