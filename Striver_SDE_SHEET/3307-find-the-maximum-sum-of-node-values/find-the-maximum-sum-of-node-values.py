class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        after = []
        for i in range(n):
            t = nums[i] ^ k
            after.append([t - nums[i], nums[i], t])
        after.sort(key = lambda x:x[0])
        def summ(array, ind):
            tot = 0
            for lists in array:
                tot += lists[ind]
            return tot
        if after[-1][0] < 0:
            return summ(after, 1)
        if after[0][0] >= 0:
            if n % 2 == 0:
                return summ(after, 2)
            return summ(after[1:], 2) + summ(after[:1], 1)
        l = bisect.bisect_left(after, [0, -1, -1])
        if after[l][0] < 0:
            l += 1
        if (n - l) % 2 == 0:
            return summ(after[l:], 2) + summ(after[:l], 1)
        if after[l - 1][0] + after[l][0] > 0:
            return summ(after[l - 1:], 2) + summ(after[:l - 1], 1)
        return summ(after[l + 1:], 2) + summ(after[:l + 1], 1)