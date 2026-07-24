class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        maxArea = 0
        i = 0

        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                right = i - 1
                left = stack[-1] if stack else -1
                area = heights[top] * (right - left)
                maxArea = max(maxArea, area)
        
        while stack:
            top = stack.pop()
            width = i - stack[-1] - 1 if stack else i
            area = heights[top] * width
            maxArea = max(maxArea, area)
        
        return maxArea