class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        l,r = 0,N-1
        while l<=r:
            mid = l+((r-l)//2)
            if nums[mid]>=target:
                r = mid-1
            else: l = mid+1
        return l

        









        