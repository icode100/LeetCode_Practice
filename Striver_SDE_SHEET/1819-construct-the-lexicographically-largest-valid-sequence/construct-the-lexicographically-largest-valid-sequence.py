class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        maxlen = ((n-1)<<1)+1
        ans = [0]*maxlen
        hashset = set()
        def recursion(i):
            if i==maxlen: return True
            if ans[i]!=0: return recursion(i+1)
            for k in range(n,0,-1):
                if k in hashset: continue
                ans[i] = k
                hashset.add(k)
                if k==1: 
                    if recursion(i+1): return True
                else:
                    if i+k<maxlen and ans[i+k]==0:
                        ans[i+k] = k
                        if recursion(i+1): return True
                        ans[i+k] = 0
                ans[i] = 0
                hashset.remove(k)
            return False
        recursion(0)
        return ans
                    


            
