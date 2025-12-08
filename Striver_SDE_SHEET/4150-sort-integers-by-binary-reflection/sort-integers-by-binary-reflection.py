class Solution:
    def reverseBits(self,num:int):
        length:int = floor(log2(num))
        if length==0: return num

        l:int
        r:int
        l,r = length,0

        while l>r:
            if (num>>r)&1 != (num>>l)&1:
                num ^= (1<<r)
                num ^= (1<<l)
            l-=1
            r+=1
            
        return num

    def sortByReflection(self, nums: List[int]) -> List[int]:
        
        return sorted(nums,key = lambda x: (self.reverseBits(x),x))