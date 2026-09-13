class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        n = len(heights)
        prefixMax = [0] * n
        suffixMax = [0] * n

        prefixMax[0] = heights[0]
        for i in range(1, n):
            currMax = max(prefixMax[i - 1], heights[i])
            prefixMax[i] = currMax
        
        suffixMax[n - 1] = heights[n - 1]
        for i in range(n - 2, -1, -1):
            currMax = max(suffixMax[i + 1], heights[i])
            suffixMax[i] = currMax

        totalArea = 0
        for i in range(n):
            area = min(prefixMax[i], suffixMax[i]) - heights[i]
            totalArea += area
        
        return totalArea