class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        ans = 0
        for i in range(49,-1,-1):
            c = comb(i,k)
            if n>c:
                n-=c
                k-=1
                ans|=(1<<i)
        return ans