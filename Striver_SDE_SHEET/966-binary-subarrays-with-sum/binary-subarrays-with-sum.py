class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap = defaultdict(int)
        sum,count = 0,0
        for r,n in enumerate(nums):
            sum+=n
            if sum==goal:count+=1
            count+=hashmap[sum-goal]
            hashmap[sum]+=1
        return count
