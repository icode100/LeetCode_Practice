class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = list()
        def recursion(index,stack,current):
            if current==target:
                ans.append(stack.copy())
                return 
            if current>target:
                return 
            if index>=len(nums):
                return 
            recursion(index+1,stack,current)
            recursion(index,stack+[nums[index]],current+nums[index])
        recursion(0,[],0)
        return ans
