class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = list()
        def recursion(index,stack):
            # if index>=len(nums):
            ans.append(stack.copy())
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]: continue
                recursion(i+1,stack+[nums[i]])
        recursion(0,[])
        return ans