class Solution:
    def compress(self, chars: List[str]) -> int:
        stack = list()
        prev = chars[0]
        count = 0
        for i,c in enumerate(chars):
            if c==prev: count+=1
            else:
                stack.append(prev)
                if count>1: 
                    for ch in str(count): stack.append(ch)
                prev = c
                count = 1

        stack.append(prev)
        if count>1: 
            for ch in str(count): stack.append(ch)
        chars[::] = stack[::]
        print(stack)
        return len(stack)

