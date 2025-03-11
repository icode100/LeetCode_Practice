class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list()
        while num:
            nums.append(num%10)
            num//=10
        nums = nums[::-1]
        n = len(nums)
        currentmax = -1
        idx = -1
        rightmax = [(-1,-1)]*n
        for i in range(n-1,-1,-1):
            if nums[i]>currentmax:
                currentmax = nums[i]
                idx = i
            if nums[i]<currentmax:
                rightmax[i] = (currentmax,idx)
        print(nums)
        print(rightmax)
        for i in range(n):
            if rightmax[i]!=(-1,-1):
                num,idx =rightmax[i]
                nums[i],nums[idx] = nums[idx],nums[i]
                break
        s = ""
        for i in nums: s+=str(i)
        return int(s)


