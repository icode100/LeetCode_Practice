class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(-inf)
        nums.insert(0,-inf)
        N = len(nums)
        l,r = 1,N-2
        while l<=r:
            mid = (l+r)//2
            if nums[mid-1]<nums[mid]>nums[mid+1]: return mid-1
            elif nums[mid-1]<nums[mid]:l = mid+1
            else: r = mid-1
        return -1

