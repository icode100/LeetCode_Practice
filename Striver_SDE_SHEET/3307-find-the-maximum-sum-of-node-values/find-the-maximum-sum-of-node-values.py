class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:

        @cache
        def recursion(i,p):
            if i==len(nums):
                return 0 if p==0 else -int(1e9)
            return max(
                (nums[i]^k)+recursion(i+1,p^1),
                nums[i]+recursion(i+1,p)
            )
        return recursion(0,0)