class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumofdigits(num):
            n = num
            ans = 0
            while n:
                ans += n%10
                n = n//10
            return ans
        hashmap = defaultdict(lambda: SortedList())
        for num in nums:
            hashmap[sumofdigits(num)].add(num)
        ans = -1
        for key in hashmap:
            if len(hashmap[key])>1:
                ans = max(ans,hashmap[key][-1]+hashmap[key][-2])
        return ans