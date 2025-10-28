class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people)
        N = len(people)
        ans = [[] for _ in range(N)]
        
        for h,k in people:
            tempk = k
            index = 0
            while tempk or ans[index]!=[]:
                if ans[index]==[] or ans[index][0]==h: tempk-=1
                index+=1
            ans[index] = [h,k]

        return ans



        
        