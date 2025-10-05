class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        N = len(nums)
        for num in nums:
            xor^=num
        setbit = (xor&(xor-1))^(xor)
        bkt1,bkt2 = 0,0
        for num in nums:
            if num&setbit: bkt1^=num
            else: bkt2^=num
        return [bkt1,bkt2]