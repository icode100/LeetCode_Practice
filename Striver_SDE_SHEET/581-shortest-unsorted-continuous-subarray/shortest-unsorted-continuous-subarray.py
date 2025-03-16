class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortednums = sorted(nums)
        n = len(nums)
        start=n
        end = 0
        stack = list()
        for i in range(n):
            while stack and nums[stack[-1]]>nums[i]:
                start = min(start,stack.pop())
            stack.append(i)
        newstack = list()
        for i in range(n-1,-1,-1):
            while newstack and nums[newstack[-1]]<nums[i]:
                end = max(end,newstack.pop())
            newstack.append(i)
        return end-start+1 if (end-start+1)>0 else 0
