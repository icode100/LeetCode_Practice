class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        N = len(nums)
        def check(k):
            mini = 0
            for i in range(0,N,k):
                if nums[i]<mini: return False
                miss = 0
                maxi = nums[i]
                for j in range(i+1,i+k):
                    maxi = max(maxi,nums[j])
                    if nums[j]<mini: return False
                    if nums[j]<nums[j-1]:
                        miss+=1
                        if miss>1: return False
                if nums[i] < nums[i + k - 1]:
                    miss += 1
                    if miss > 1:
                        return False
                mini = maxi
            return True
        count = 0
        for k in range(1,N+1):
            if N%k==0 and check(k):
                count+=k
        return count