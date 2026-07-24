class Solution:
    # TC:O(N), SC:O(N)
    # def findBuildings(self, heights: List[int]) -> List[int]:
    #     stack = []
        
    #     for i, h in enumerate(heights):
    #         while stack and heights[stack[-1]] <= h:
    #             stack.pop()
    #         stack.append(i)
    #     return stack
    
    # TC:O(N), SC:O(1)
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        maxHeight = -1

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > maxHeight:
                result.append(i)
                maxHeight = heights[i]
        result.reverse()
        return result