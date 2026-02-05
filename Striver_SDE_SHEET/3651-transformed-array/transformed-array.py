class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [-inf]*N
        for i,num in enumerate(nums):
            result[i] = nums[(num+i)%N]
        return result
            