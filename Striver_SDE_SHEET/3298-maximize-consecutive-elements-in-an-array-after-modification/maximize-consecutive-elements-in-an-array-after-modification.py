class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        '''
        * as the nums[i]<1e6 so state can be defined in terms of nums[i] rather than i
        * dp[k] = longest sequence ending at k
        * as we are approaching in an increasing order and the order of elements in the array do not matter so we can sort it
        '''
        nums.sort()
        dp = defaultdict(int)
        # def recursion(i):
        N = len(nums)
        for i in range(N):   
            num = nums[i]
            prev_num = dp[num]
            prev_num_1 = dp[num-1]
            dp[num] = max(prev_num_1+1,dp[num])
            dp[num+1] = max(prev_num+1,dp[num+1])
        return max(dp.values())

            