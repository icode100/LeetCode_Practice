class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()
        for i in asteroids:
            while stack and i<0 and stack[-1]>0 and abs(stack[-1])<abs(i):
                stack.pop()
            if stack and i<0 and stack[-1]>0 :
                if abs(stack[-1])==abs(i):
                    stack.pop()
                continue
            stack.append(i)
        return stack