class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        while len(nums)>1:
            heap = list()
            flag = True
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]: flag = False
                heappush(heap,(nums[i]+nums[i+1],i))
            
            if flag: break

            minval,minidx = heappop(heap)
            nums[minidx] = minval
            nums.pop(minidx+1)
            count+=1
        
        return count
            