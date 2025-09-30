class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = list()
        def recursion(index,stack):
            if index==N:
                ans.append(stack.copy())
                return 
            recursion(index+1,stack)
            recursion(index+1,stack+[nums[index]])
        recursion(0,[])
        return ans
