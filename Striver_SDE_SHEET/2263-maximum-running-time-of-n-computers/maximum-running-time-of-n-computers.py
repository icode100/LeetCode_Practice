class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        def check(mid):
            current = sum(min(p,mid) for p in batteries)
            return current//n >= mid

        l,r = 1,sum(batteries)//n

        while l<r:
            mid = r - (r-l)//2

            if check(mid): l = mid
            else: r = mid-1
        
        return l