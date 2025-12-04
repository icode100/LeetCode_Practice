class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = list()
        count = 0
        for c in directions:
            if not stack: stack.append(c)
            else:
                if c=='L' and stack[-1]=='R':
                    count+=1
                    while stack and stack[-1]=='R':
                        count+=1
                        stack.pop()
                    stack.append('S')
                elif c=='S':
                    while stack and stack[-1]=='R':
                        stack.pop()
                        count+=1
                    stack.append('S')
                elif c=='L' and stack[-1]=='S':
                    count+=1
                    stack.append('S')
                else: stack.append(c)
        return count