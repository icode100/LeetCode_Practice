class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        if N==1: return nums[0]
        l,r = 0,N-1
        while l<=r:
            if l==r: return nums[l]
            mid = (l+r)//2
            if mid&1==0:
                if (l<mid<r and nums[mid-1] != nums[mid]!=nums[mid+1]): return mid
                if l==mid and nums[mid]!=nums[mid+1]: return mid
                if r==mid and nums[mid]!=nums[mid-1]: return mid
                mid-=1
            if nums[mid]==nums[mid-1]: l = mid+1
            else: r = mid-1
        return -1