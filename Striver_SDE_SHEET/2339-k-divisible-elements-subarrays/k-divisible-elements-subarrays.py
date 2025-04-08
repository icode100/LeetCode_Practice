class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        N = len(nums)
        ans = 0
        count = 0
        l = 0
        hashset = set()
        for r in range(N):
            count+=int((nums[r]%p)==0)
            while l<r and count>k:
                count-=int((nums[l]%p)==0)
                l+=1
            string = ""
            for i in range(l,r+1):
                hashset.add(tuple(nums[i:r+1]))
        return len(hashset)

