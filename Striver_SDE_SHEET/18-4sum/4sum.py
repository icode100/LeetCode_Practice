class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        N = len(nums)
        for i in range(N):
            for j in range(i+1,N):
                l,r = j+1,N-1
                while l<r:
                    current = nums[l]+nums[r]+nums[i]+nums[j]
                    if current>target: r-=1
                    elif current<target: l+=1
                    else:
                        ans.add((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                        r-=1
        return [list(num) for num in ans]


