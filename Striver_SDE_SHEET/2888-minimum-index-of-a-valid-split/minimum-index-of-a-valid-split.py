class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter()
        maxf,maxnum = 0,0
        for i,num in enumerate(nums):
            counter[num]+=1
            if counter[num]>maxf:
                maxf = counter[num]
                maxnum = num
        left = 0
        for i in range(n):
            if nums[i]==maxnum:
                left+=1
            if left>(i+1)//2 and (maxf-left) > (n-i-1)//2: return i
        return -1
        
