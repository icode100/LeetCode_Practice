class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        mini = nums[k]
        n = len(nums)
        i = j = k
        ans = nums[k]
        while i>0 or j<n-1:
            if (nums[i-1] if i>0 else 0) < (nums[j+1] if j<n-1 else 0):
                j+=1
                mini = min(mini,nums[j])
            else:
                i-=1
                mini = min(mini,nums[i])
            ans = max(ans,mini*(j-i+1))
        return ans

            