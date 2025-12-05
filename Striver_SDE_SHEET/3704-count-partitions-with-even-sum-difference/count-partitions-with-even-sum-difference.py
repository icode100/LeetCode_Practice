class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total:int = sum(nums)
        current:int = 0
        count:int = 0
        N:int = len(nums)

        for i in range(N-1):
            current+=nums[i]
            if (total-2*current)&1==0: count+=1
        
        return count
