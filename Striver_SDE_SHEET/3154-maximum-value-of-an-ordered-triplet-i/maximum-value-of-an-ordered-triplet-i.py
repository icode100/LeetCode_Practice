class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        '''
        * we need to maximize so multiplier shall have the highest weight
        * so let's fix nums[k]
        * for each nums[k] lets find maxelement to the left and minelement to the right of that but not exceeding nums[k]
        * but if we fix nums[k] it will be hard to find nums[j] and nums[i] both at a time with certainity
        * so better to fix nums[j]
        '''
        n = len(nums)
        max_l,max_r = [nums[0]],deque([nums[-1]])
        for i in range(1,n):
            if nums[i]>max_l[-1]: max_l.append(nums[i])
            else: max_l.append(max_l[-1])
        for i in range(n-1,0,-1):
            if nums[i]>max_r[0]: max_r.appendleft(nums[i])
            else: max_r.appendleft(max_r[0])
        max_l[0],max_r[-1] = [-inf,-inf]
        for i in range(n):
            ans = max(ans,(max_l[i]-nums[i])*max_r[i])
        return ans