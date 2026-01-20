class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def findCompliment(num):
            x = num
            cnt = 0
            oo = ((x+1)^x)&x
            k = int(log2(oo+1))
            oo = (oo>>1)
            x = ((x>>k)<<k)
            return x|oo


        ans = list()
        for num in nums:
            if num==2:
                ans.append(-1)
            else:
                ans.append(findCompliment(num))
        return ans