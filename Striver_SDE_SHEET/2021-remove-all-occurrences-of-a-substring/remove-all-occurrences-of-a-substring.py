class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = list()
        M = len(part)
        N = len(s)
        check = lambda:"".join(stack[-M:]) == part
        for i in range(N):
            stack.append(s[i])
            if len(stack)>=M and check(): stack = stack[:-M]                
        return "".join(stack)
            