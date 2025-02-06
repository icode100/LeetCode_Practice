class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        checker = set(nums)
        result = inf
        start = min(nums)
        end = max(nums)
        if end<1:
            return 1
        if start>1:
            return 1
        for i in range(1,10**5+2):
            if i not in checker:
                return i
        


