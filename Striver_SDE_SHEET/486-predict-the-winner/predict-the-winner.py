class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def recursion(left,right):
            if left>right: return 0
            return max(nums[left]-recursion(left+1,right), nums[right]-recursion(left,right-1))
        return recursion(0,n-1)>=0