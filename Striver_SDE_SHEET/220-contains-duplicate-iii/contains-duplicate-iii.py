class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        bucket = {}
        for i in range(len(nums)):
            index = nums[i]//(valueDiff+1)
            if index in bucket and abs(bucket[index]-nums[i])<=valueDiff: return True
            if index+1 in bucket and abs(bucket[index+1]-nums[i])<=valueDiff: return True
            if index-1 in bucket and abs(bucket[index-1]-nums[i])<=valueDiff: return True
            bucket[index] = nums[i]
            if i>=indexDiff: bucket.pop(nums[i-indexDiff]//(valueDiff+1))
        return False