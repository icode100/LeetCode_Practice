class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        @cache
        def recursion(num):
            if num<=0: return 0
            return max(counter[num]*num+recursion(num-2), recursion(num-1))
        return recursion(max(nums))