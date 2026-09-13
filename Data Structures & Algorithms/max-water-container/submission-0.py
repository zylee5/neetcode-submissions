class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxArea = float('-inf')

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            maxArea = max(maxArea, area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return maxArea