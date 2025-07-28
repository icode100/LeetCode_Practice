class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # pick and not pick
        # whenver we or two elem the value will always increase or remain the same as the max among the two
        N = len(nums)
        maxor = list(accumulate(nums,operator.or_))[-1]
        count = 0
        def recursion(index,curror):
            nonlocal count
            if index>=N: 
                if curror==maxor: count+=1
                return 
            recursion(index+1,curror)
            recursion(index+1,curror|nums[index])
        recursion(0,0)
        return count


        return 0