class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        currentMax = 0

        for i in range(len(heights)):

            for j in range(i, len(heights)):
                area = (j-i) * min(heights[i], heights[j])
                currentMax = max(currentMax,area)

        return currentMax