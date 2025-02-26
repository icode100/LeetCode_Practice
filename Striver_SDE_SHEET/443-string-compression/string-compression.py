class Solution:
    def compress(self, chars: List[str]) -> int:
        stack=[]
        s=""
        for i in range(len(chars)):
            if len(stack)==0 or stack[-1]==chars[i]:
                stack.append(chars[i])
            else:
                s+=stack[-1]
                if len(stack)!=1:
                    s+=str(len(stack))
                stack.clear()
                stack.append(chars[i])
        s+=stack[-1]
        if len(stack)!=1:
            s+=str(len(stack))
        chars.clear()
        for i in s:
            chars.append((i))
        return len(s)

        