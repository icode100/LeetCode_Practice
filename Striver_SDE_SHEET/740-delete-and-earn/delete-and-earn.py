class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        @cache
        def recursion(i):
            if i<=0: return 0
            pick = counter[i]*i + recursion(i-2)
            notpick = recursion(i-1)
            return max(pick,notpick)
        return recursion(max(counter.keys()))


        
