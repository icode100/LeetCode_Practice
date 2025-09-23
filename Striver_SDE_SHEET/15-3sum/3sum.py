class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        ans = []
        for i in range(N):
            if i>0 and nums[i]==nums[i-1]: continue
            j,k = i+1,N-1
            while j<k:
                temp = nums[i]+nums[j]+nums[k]
                if temp<0: j+=1
                elif temp>0: k-=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:j+=1
                    while j<k and nums[k]==nums[k+1]:k-=1

        return ans