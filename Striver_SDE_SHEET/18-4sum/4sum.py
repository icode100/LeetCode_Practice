class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(n):
            # if i>0 and nums[i]==nums[i-1]:continue
            for l in range(i+1,n):
                # if i>0 and nums[l]==nums[l-1]:continue
                j = l+1
                k = n-1
                while j<k:
                    sumi = nums[i]+nums[j]+nums[k]+nums[l]
                    if sumi<target:
                        j+=1
                    elif sumi>target:
                        k-=1
                    else:
                        ans.add((nums[i],nums[l],nums[j],nums[k]))
                        j+=1
                        k-=1
                        # while j<k and nums[j]==nums[j-1]:j+=1
                        # while j<k and nums[k]==nums[k+1]:k-=1
        return [list(nums) for nums in ans]