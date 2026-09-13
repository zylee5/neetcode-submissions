class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        n = len(heights)
        prefixMax = [0] * n
        suffixMax = [0] * n

        currMax = heights[0]
        prefixMax[0] = currMax
        for i in range(1, n):
            currMax = max(currMax, heights[i])
            prefixMax[i] = currMax
        
        currMax = heights[n - 1]
        suffixMax[n - 1] = currMax
        for i in range(n - 2, -1, -1):
            currMax = max(currMax, heights[i])
            suffixMax[i] = currMax

        totalArea = 0
        for i in range(n):
            area = min(prefixMax[i], suffixMax[i]) - heights[i]
            totalArea += area
        
        return totalArea