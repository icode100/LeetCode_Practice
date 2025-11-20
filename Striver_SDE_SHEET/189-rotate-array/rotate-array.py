class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums)
        ans = [0]*N
        k %= N
        for i in range(N):
            ans[(i+k)%N] = nums[i]
        nums[::] = ans[::]
        