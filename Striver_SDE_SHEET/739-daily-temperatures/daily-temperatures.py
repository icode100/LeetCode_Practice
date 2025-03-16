class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        nextGreater = [0]*n
        stack = list()
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                idx = stack.pop()
                nextGreater[idx] = i-idx
            stack.append(i)

        return nextGreater
