class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        def count(left,right):
            nonlocal ans
            i,j = 0,0
            flag = 0
            while i < len(left) and j < len(right):
                if left[i] > 2 * right[j]:  
                    ans += len(left) - i  # All remaining left[i:] will satisfy the condition
                    j += 1
                else:
                    i += 1
            

        def merge(left,right):
            i,j = 0,0
            merged = list()
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    merged.append(left[i])
                    i+=1
                else: 
                    merged.append(right[j])
                    j+=1
            if i<len(left): merged.extend(left[i:])
            if j<len(right): merged.extend(right[j:])
            return merged

            
        def recursion(nums):
            nonlocal ans
            if len(nums)==1: return nums
            mid = len(nums)>>1
            left = recursion(nums[:mid])
            right = recursion(nums[mid:])
            count(left,right)
            return merge(left,right)

        recursion(nums)
        return ans