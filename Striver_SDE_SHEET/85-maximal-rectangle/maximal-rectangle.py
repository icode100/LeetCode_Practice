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
        # print(leftsmall,rightsmall)
        ans = 0
        for i in range(N):
            ans = max(ans,(rightsmall[i]-leftsmall[i]+1)*heights[i])
        return ans
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
        for j in range(len(matrix[0])):
            for i in range(1,len(matrix)):
                if matrix[i][j]==0: continue
                else:
                    matrix[i][j]+=matrix[i-1][j]
        return max(self.largestRectangleArea(matrix[i]) for i in range(len(matrix)))



