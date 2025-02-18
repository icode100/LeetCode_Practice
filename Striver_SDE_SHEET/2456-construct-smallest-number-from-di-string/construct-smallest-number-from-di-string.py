class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        stack = list()
        i = 0
        while i<n and pattern[i]!='I': i+=1
        stack.append(i+1)
        maxval = stack[-1]
        i = 0
        while i<n:
            if pattern[i]=='I':
                if i+1<n and pattern[i+1]=='D':
                    j = maxval
                    idx = i+1
                    while idx<n and pattern[idx]!='I': 
                        j+=1
                        idx+=1
                    stack.append(j+1)
                else: stack.append(maxval+1)
            else:
                # if i+1<n and pattern[i+1]=='I':
                #     j = stack[-1]
                #     idx = i+1
                #     while idx<n and pattern[idx]!='D':
                #         j-=1
                #         idx+=1
                #     stack.append(j-1)
                stack.append(stack[-1]-1)
            maxval = max(maxval,stack[-1])
            i+=1
        # print(stack)
        return ''.join(list(map(str,stack)))
                    
                

        
