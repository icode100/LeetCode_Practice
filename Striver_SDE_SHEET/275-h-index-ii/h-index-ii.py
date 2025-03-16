class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(mid):
            count = 0
            for i in citations:
                if i>=mid: count+=1
            return count>=mid
        left,right = 1,len(citations)
        while left<=right:
            mid = (left+right)>>1
            if check(mid):
                left = mid+1
            else:
                right = mid-1
        return right

