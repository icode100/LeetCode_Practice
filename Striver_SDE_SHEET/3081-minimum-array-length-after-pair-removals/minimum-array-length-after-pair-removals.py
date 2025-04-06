class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        median = ceil(len(nums)/2)
        r = median
        removed = set()
        while l<r and r<n:
            if nums[l]<nums[r] and l not in removed:
                removed.add(l)
                removed.add(r)
                l+=1
            r+=1
        return len(nums)-len(removed)

                