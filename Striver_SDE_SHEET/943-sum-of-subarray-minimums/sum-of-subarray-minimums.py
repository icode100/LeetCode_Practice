class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        n = len(nums)
        arr_left = [0]*n
        arr_right = [n-1]*n
        stack = list()
        for i in range(n):
            while stack and nums[i]<=nums[stack[-1]]:
                arr_right[stack.pop()] = i-1
            stack.append(i)
        stack.clear()
        for i in range(n-1,-1,-1):
            while stack and nums[i]<nums[stack[-1]]:
                arr_left[stack.pop()] = i+1
            stack.append(i)
        # print(arr_left, arr_right)

        return int(sum((nums[i]*(abs(i-arr_left[i])+1)*(abs(arr_right[i]-i)+1))%(1e9+7) for i in range(n))%(1e9+7))

