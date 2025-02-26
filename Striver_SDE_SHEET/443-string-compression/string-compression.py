class Solution:
    def compress(self, chars: List[str]) -> int:
        stack = list()
        ans = list()
        for i in chars:
            if not stack or stack[-1]==i: stack.append(i)
            elif i!=stack[-1]:
                top = stack[-1]
                count = 0
                while stack:
                    stack.pop()
                    count+=1
                ans.append(top)
                if count!=1: 
                    for c in str(count):ans.append(c)
                stack.append(i)
        top = stack[-1]
        count = 0
        while stack:
            stack.pop()
            count+=1
        ans.append(top)
        if count!=1: 
            for c in str(count):ans.append(c)
        print(ans)
        for i in range(len(ans)): chars[i] = ans[i]
        return len(ans)