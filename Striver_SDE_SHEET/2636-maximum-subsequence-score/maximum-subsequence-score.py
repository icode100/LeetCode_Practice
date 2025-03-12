class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        pairs = sorted(zip(nums1,nums2), key = lambda x:(-x[1],-x[0]))
        heap,sumi,ans = list(),0,0
        for num1,num2 in pairs:
            sumi+=num1
            heappush(heap,num1)
            if len(heap)>k: sumi-=heappop(heap)
            if len(heap)==k:ans = max(ans,sumi*num2)
        return ans

        