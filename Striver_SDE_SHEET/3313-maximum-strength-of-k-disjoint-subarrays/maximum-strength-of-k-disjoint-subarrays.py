class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        N = len(nums)

        @cache
        def recursion(i,k,flag):
            if k==0: return 0
            if i==N: return -inf
            if not flag: return max(
                recursion(i+1,k,False),
                ((-1)**((k+1)&1))*k*nums[i]+ max(
                    recursion(i+1,k-1,True),
                    recursion(i+1,k,True)
                )
            )
            else:
                return ((-1)**((k+1)&1))*k*nums[i]+ max(
                    recursion(i+1,k-1,True),
                    recursion(i+1,k,True)
                )
        
        ans = recursion(0,k,False)
        recursion.cache_clear()
        return ans

            
        


                