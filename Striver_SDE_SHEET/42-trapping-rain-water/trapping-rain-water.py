class Solution:
    def trap(self, nums: List[int]) -> int:
        N = len(nums)
        left = 0
        right = N-1
        leftmax,rightmax = nums[left],nums[right]
        ans = 0
        while left<right:
            if leftmax<rightmax:
                left+=1
                leftmax = max(leftmax,nums[left])
                ans+=leftmax-nums[left]
            else:
                right-=1
                rightmax = max(rightmax,nums[right])
                ans+=rightmax-nums[right]
        return ans



