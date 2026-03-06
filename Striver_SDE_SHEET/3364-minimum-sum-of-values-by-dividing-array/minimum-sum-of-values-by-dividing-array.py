class Solution:
    def minimumValueSum(self, nums: List[int], andVal: List[int]) -> int:
        '''
        * dp(i,j, current)  = min val till i in nums and j in andVal with and value as current
        * i<j never possible 
        * always i>=j
        * when current == andVal[j] we have two options
            * nums[i]+recursion(i+1,j+1,1)
            * recursion(i+1,j,current+nums[i])
        * and of two numbers is always <= the smaller number so if current<andVal[j] return inf
        '''
        N = len(nums)
        M = len(andVal)
        @cache
        def recursion(i,j,current):
            if i==N: return 0 if j==M else inf
            if j==M: return inf
            newcurrent = current&nums[i]
            if newcurrent<andVal[j]: return inf
            return min(
               nums[i] + recursion(i+1,j+1,(1<<20)-1) if newcurrent==andVal[j] else inf,
               recursion(i+1,j,newcurrent)
            )
        ans = recursion(0,0,(1<<20)-1)
        return ans if ans != inf else -1