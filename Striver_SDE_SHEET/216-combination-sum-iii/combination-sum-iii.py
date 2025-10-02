class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = list()
        def recursion(index,stack,current):
            if current>n:return
            if len(stack)==k:
                if current==n: ans.append(stack.copy())
                return 
            if current==n: return
            for i in range(index,10):
                if i+current<=n:
                    recursion(i+1,stack+[i],current+i)
        recursion(1,[],0)
        return ans
