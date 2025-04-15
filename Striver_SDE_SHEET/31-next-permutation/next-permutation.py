class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        '''
        current => 1 2 4 6 5 3
        next    => 1 2 5 3 4 6 

        observations: 
        * 4 is the pivotal point prefix till 4 remains the same 
        * because idx = index(4) is the first index starting from the end of array where nums[idx]<nums[idx+1]
        * now 4 should be swapped with the absolute next greater element in the suffix from index(4).
        * making 1 2 5 6 4 3
        * now we arrange the suffix in ascending order making it [1 2 5 3 6 4]
        '''
        N = len(nums)
        idx = -1
        for i in range(N-2,-1,-1):
            if nums[i]<nums[i+1]: 
                idx = i
                break
        if idx==-1: 
            nums[::1] = nums[::-1]
            return 
        for i in range(N-1,idx,-1):
            if nums[i]>nums[idx]:
                nums[i],nums[idx] = nums[idx], nums[i]
                break
        print(idx, nums[:idx+1])
        nums[::1] = nums[:idx+1]+sorted(nums[idx+1:])