class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = list()
        res = [-1]*n
        for i in range(n*2):
            num,i = nums[i%n],i%n
            while stack and num>nums[stack[-1]]:
                res[stack.pop()] = num
            stack.append(i)
        return res