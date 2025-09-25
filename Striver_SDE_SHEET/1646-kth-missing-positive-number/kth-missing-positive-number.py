class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l,r = 0,N-1
        while l<=r:
            mid = (l+r)//2
            if (nums[mid]-mid-1)<k: l = mid+1
            else: r = mid-1
        return l+k