class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even,odd,ans = 1,0,0
        current = 0
        for i in arr:
            current+=i
            if current&1:
                odd+=1
                ans+=even
            else: 
                even+=1
                ans+=odd

        return ans%int(1e9+7)