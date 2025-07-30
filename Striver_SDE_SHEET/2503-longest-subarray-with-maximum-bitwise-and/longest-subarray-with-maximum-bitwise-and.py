class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # if you do an and then the result will always be smaller than or equal to the smaller number among the two
        maxand = max(nums)
        N = len(nums)
        temp = 0
        net = 0
        for i in range(N):
            if nums[i]==maxand: temp+=1
            else:
                net = max(net,temp)
                temp=0
        net = max(net,temp)
        return net

        