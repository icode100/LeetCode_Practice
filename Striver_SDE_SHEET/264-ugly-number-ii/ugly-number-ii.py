class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        ans = 0
        vis = {1}
        while n:
            ans = heappop(heap)
            n-=1
            if not n: return ans
            for i in [2,3,5]:
                if ans*i not in vis: 
                    heappush(heap,ans*i)
                    vis.add(ans*i)
        return ans
