class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        N = len(nums1)
        oddset = sorted({nums1[i] for i in range(N) if nums1[i]&1})
        evenset = sorted({nums1[i] for i in range(N) if not nums1[i]&1})
        canbeodd = True
        canbeeven = True
        for i in range(N):
            if nums1[i]&1: continue
            else:
                if len(oddset)>0 and nums1[i]-oddset[0]>=1: continue
                else:
                    canbeodd = False
                    break
        for i in range(N):
            if nums1[i]&1==0: continue
            else:
                if len(oddset)>0 and nums1[i]-oddset[0]>=1:
                    continue
                else:
                    canbeeven = False
                    break
        return canbeodd or canbeeven
