class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        minprefix,maxprefix = 0,0
        maxi,mini = -1e6,1e6
        current = 0
        for i in range(n):
            current+=nums[i]
            maxi,mini = max(maxi,current-minprefix),min(mini,current-maxprefix)
            maxprefix,minprefix = max(maxprefix,current),min(minprefix,current)
        print(maxi,mini,current)
        return max(maxi,current-mini) if maxi>0 else maxi


