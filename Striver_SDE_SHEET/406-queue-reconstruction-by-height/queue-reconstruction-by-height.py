class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        ans = [[] for i in range(n)]
        # heapify(people)
        for h,k in sorted(people):
            height,pos = h,k
            k = pos
            i = 0
            while k or ans[i]!=[]:
                if ans[i]==[] or ans[i][0]>=height:
                    k-=1
                i+=1
            ans[i] = [height,pos]
        return ans