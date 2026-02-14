class Solution:
    def minNumberOperations(self, nums: List[int]) -> int:
        '''
        * we need to do atleast min(target) ops
        * for every element if its greater than current max then we need to perform operations else it would have already been taken care of

        '''
        ans = nums[0]
        currentmax = ans
        for i in range(1,len(nums)):
            if nums[i]>currentmax: ans+=nums[i]-currentmax
            currentmax = nums[i]
        return ans

        
