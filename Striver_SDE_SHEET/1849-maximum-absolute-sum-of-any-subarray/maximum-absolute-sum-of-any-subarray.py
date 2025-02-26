class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def kadane(nums):
            ans,current = 0,0
            for i in nums:
                current+=i
                if current<0: current = 0
                ans = max(ans,current)
            return ans
        minnums = [-i for i in nums]
        return max(kadane(minnums),kadane(nums))