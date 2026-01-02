class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mask:int = 0
        for num in nums:
            num:int
            newbit:int = (1<<num)
            
            if (mask&newbit) != 0:
                return num

            mask = (mask | newbit)

            print(mask)
        
        return -1
