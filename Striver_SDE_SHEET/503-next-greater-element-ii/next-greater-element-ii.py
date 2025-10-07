class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = list()
        N = len(nums)
        mapper = {}
        for i in range(N*2):
            while stack and nums[i%N]>nums[stack[-1]%N]:
                mapper[stack.pop()%N] = nums[i%N]
            stack.append(i)
        return [mapper[i] if i in mapper else -1 for i in range(N)]