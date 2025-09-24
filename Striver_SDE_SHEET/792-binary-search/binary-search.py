class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        l,r = 0,N-1
        while l<=r:
            mid = l+((r-l+1)//2)
            # print(mid)
            if nums[mid]==target: return mid
            if nums[mid]>target: r=mid-1
            else: l = mid+1
        return -1