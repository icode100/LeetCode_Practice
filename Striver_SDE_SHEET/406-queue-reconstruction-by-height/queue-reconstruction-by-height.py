class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people,key = lambda x:(x[1],-x[0]))
        ans = deque()
        stack = list()
        for h,k in people:
            if not ans: ans.append([h,k])
            else:
                tempk = k
                while ans and k>0:
                    if ans[0][0]>=h: k-=1
                    stack.append(ans.popleft())
                ans.appendleft([h,tempk])
                while stack:
                    ans.appendleft(stack.pop())
        return list(ans)



        
        