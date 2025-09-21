class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg = 0,0
        while nums[pos]<0: pos+=1
        while nums[neg]>0: neg+=1
        N = len(nums)
        ans = []
        while len(ans)<N:
            if len(ans)&1==0:
                ans.append(nums[pos])
                pos+=1
                while pos<N and nums[pos]<0: pos+=1
            else:
                ans.append(nums[neg])
                neg+=1
                while neg<N and nums[neg]>0: neg+=1
        return ans