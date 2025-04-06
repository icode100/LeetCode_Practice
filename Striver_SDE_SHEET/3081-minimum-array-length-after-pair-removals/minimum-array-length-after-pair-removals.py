class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        x = max(Counter(nums).values())
        if x>(N>>1): return x-(N-x)
        return N&1
        

                