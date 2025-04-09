class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        N = len(nums)
        count = 1
        for r in range(1,N):
            if nums[r]==nums[r-1]: count+=1
            else: count = 1
            if count<=2:
                nums[l] = nums[r]
                l+=1
        return l
