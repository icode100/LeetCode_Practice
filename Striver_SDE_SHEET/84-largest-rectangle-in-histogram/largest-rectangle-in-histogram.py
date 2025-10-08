class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        stack = list()
        leftsmall = [0]*N
        rightsmall = [N-1]*N
        for i,height in enumerate(heights):
            while stack and heights[stack[-1]]>height:
                rightsmall[stack.pop()] = i-1
            stack.append(i)
        stack.clear()
        for i in range(N-1,-1,-1):
            height = heights[i]
            while stack and heights[stack[-1]]>height:
                leftsmall[stack.pop()] = i+1
            stack.append(i)
        print(leftsmall,rightsmall)
        ans = 0
        for i in range(N):
            ans = max(ans,(rightsmall[i]-leftsmall[i]+1)*heights[i])
        return ans
        