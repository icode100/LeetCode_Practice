class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [0]*k
        current = 0
        count = 0

        for i,num in enumerate(nums):
            current += num

            if current%k==0: count+=1
            count += prefix[current%k]

            prefix[current%k]+=1
        
        return count

            