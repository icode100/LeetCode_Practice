class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        N = len(nums1)
        oddset = {i for i in range(N) if nums1[i]&1}
        evenset = {i for i in range(N) if not nums1[i]&1}
        canbeodd = True
        canbeeven = True

        for i in range(N):
            if nums1[i]&1: continue
            else:
                if len(oddset)>0: continue
                else:
                    canbeodd = False
                    break
        for i in range(N):
            if nums1[i]&1==0: continue
            else:
                if len(oddset)>0:
                    if len(oddset)>1: continue
                    if len(oddset)==1:
                        if i in oddset: 
                            canbeeven = False
                            break
                else:
                    canbeeven = False
                    break
        return canbeodd or canbeeven
