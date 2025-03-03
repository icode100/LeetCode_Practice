class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        i,j = 0,n-1
        ans = [-1e9]*n
        left,right = 0,n-1
        while i<n and j>-1:
            if nums[i]<pivot:
                ans[left] = nums[i]
                i+=1
                left+=1
            elif nums[i]>=pivot:
                i+=1
            if nums[j]>pivot:
                ans[right] = nums[j]
                right-=1
                j-=1
            elif nums[j]<=pivot:
                j-=1
        while left<=right:
            ans[left] = pivot
            left+=1
        return ans

        
