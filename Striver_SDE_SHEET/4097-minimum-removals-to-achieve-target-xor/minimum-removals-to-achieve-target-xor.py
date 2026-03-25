class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        N = len(nums)

        @cache
        def recursion(index,current):
            if index==N:
                if current==target: return 0
                return inf
            return min(
                1+recursion(index+1,current),
                recursion(index+1,current^nums[index])
            )
        ans = recursion(0,0)
        recursion.cache_clear()
        return ans if ans!=inf else -1