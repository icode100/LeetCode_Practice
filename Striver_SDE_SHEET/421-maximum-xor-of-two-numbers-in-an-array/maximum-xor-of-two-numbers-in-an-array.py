class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor=0
        mask=0
        for i in range(31,-1,-1):
            mask = mask |  (1<<i)
            pref=set()
            for num in nums:
                pref.add(num & mask)

            temp= max_xor | (1<<i)

            for p in pref:
                if (temp^p) in pref:
                    max_xor=temp

                    break
        return max_xor




        