class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        ans = 0
        prefix = [0]*n
        suffix = [0]*n

        sumi = 0
        for i in range(n):
            if i<firstLen:
                sumi+=nums[i]
                prefix[i] =sumi
            else:
                sumi+=nums[i]
                sumi-=nums[i-firstLen]
                prefix[i] =max(prefix[i-1],sumi)
        sumi = 0
        for i in range(n-1,-1,-1):
            if i+secondLen>=n:
                sumi+=nums[i]
                suffix[i] = sumi
            else:
                sumi+=nums[i]
                sumi-=nums[i+secondLen]
                suffix[i] = max(suffix[i+1],sumi)
        for i in range(firstLen-1,n-secondLen):
            ans = max(ans,prefix[i]+suffix[i+1])
        prefix = [0]*n
        suffix = [0]*n

        sumi = 0
        for i in range(n):
            if i<secondLen:
                sumi+=nums[i]
                prefix[i] =sumi
            else:
                sumi+=nums[i]
                sumi-=nums[i-secondLen]
                prefix[i] =max(prefix[i-1],sumi)
        sumi = 0
        for i in range(n-1,-1,-1):
            if i+firstLen>=n:
                sumi+=nums[i]
                suffix[i] = sumi
            else:
                sumi+=nums[i]
                sumi-=nums[i+firstLen]
                suffix[i] = max(suffix[i+1],sumi)
        for i in range(secondLen-1,n-firstLen):
            ans = max(ans,prefix[i]+suffix[i+1])
        return ans
