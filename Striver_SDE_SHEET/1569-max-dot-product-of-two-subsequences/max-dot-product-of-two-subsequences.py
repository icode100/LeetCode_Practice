class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        N1,N2 = len(nums1),len(nums2)
        if max(nums1)<0 and min(nums2)>0: return max(nums1)*min(nums2)
        if min(nums1)>0 and max(nums2)<0: return min(nums1)*max(nums2)

        @cache
        def recursion(i,j):
            if i>=N1 or j>=N2: return 0

            pick = nums1[i]*nums2[j] + recursion(i+1,j+1)
            notpick = max(recursion(i+1,j),recursion(i,j+1))

            return max(pick, notpick)
        
        return recursion(0,0)