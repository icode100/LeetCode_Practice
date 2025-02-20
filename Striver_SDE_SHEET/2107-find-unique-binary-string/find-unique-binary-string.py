class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        setnum = set(nums)
        for num in range(len(nums)+2):
            val = bin(num)[2:].zfill(n)
            if val not in setnum: return val