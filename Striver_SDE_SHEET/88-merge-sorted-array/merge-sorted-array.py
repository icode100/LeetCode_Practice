class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1
        ptr = m+n-1
        while ptr>=0:
            if i>=0 and j>=0 and nums1[i]>nums2[j]:
                nums1[ptr] = nums1[i]
                i-=1
            elif j>=0:
                nums1[ptr] = nums2[j]
                j-=1
            ptr -=1


        