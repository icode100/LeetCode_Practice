class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        stack = list()
        for num in nums:
            while stack and num*stack[-1]<0 and (stack[-1]>0 and num<0) and abs(num)>abs(stack[-1]): stack.pop()
            if stack and num*stack[-1]<0 and (stack[-1]>0 and num<0) and abs(num)<abs(stack[-1]): 
                continue
            elif stack and num*stack[-1]<0 and (stack[-1]>0 and num<0) and abs(num)==abs(stack[-1]):
                stack.pop()
                continue
            stack.append(num)
        return stack