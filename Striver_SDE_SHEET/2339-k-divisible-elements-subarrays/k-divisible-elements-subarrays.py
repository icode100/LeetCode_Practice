class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        cnt = 0
        n = len(nums)
        start = 0
        hashing = set()
        for end in range(n):
            if nums[end]%p==0:
                cnt+=1
            while cnt>k and start<end:
                for i in range(start+1,end+1):hashing.add(tuple(nums[start:i]))
                if not nums[start]%p: cnt-=1
                start+=1
        end+=1
        while start<end:
            for i in range(start+1,end+1):hashing.add(tuple(nums[start:i]))
            start+=1
        return len(hashing)