mod = int(1e9+7)
fact = defaultdict(lambda:1)
invfact = defaultdict(lambda:1)
for i in range(2, 10**5 + 1): fact[i] = (fact[i - 1] * i) % mod
invfact[10**5] = pow(fact[10**5], mod - 2, mod)  

for i in range(10**5 - 1, 0, -1): invfact[i] = (invfact[i + 1] * (i + 1)) % mod

invfact[0] = 1  

def comb_(n, r):
    if r < 0 or r > n:
        return 0
    return (fact[n] * invfact[r] % mod) * invfact[n - r] % mod

class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            val = nums[i]
            minmul = 1
            maxmul = 1
            for j in range(1, k):
                minmul = (minmul + comb_(n - i - 1, j)) % mod
                maxmul = (maxmul + comb_(i, j)) % mod
            ans = (ans + nums[i] * (minmul + maxmul)) % mod
        return ans
