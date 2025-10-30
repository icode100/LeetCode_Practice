class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def recursion(index):
            if index>=len(nums): return 0
            return max(recursion(index+1),nums[index]+recursion(index+2))
        return recursion(0)