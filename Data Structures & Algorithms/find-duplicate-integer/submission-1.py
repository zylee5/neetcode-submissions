class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            lessOrEqual = 0
            for num in nums:
                if num <= mid:
                    lessOrEqual += 1
            
            if lessOrEqual > mid:
                # Too many numbers in 1...mid
                # Duplicate must be here
                high = mid
            else:
                # No duplicate in 1...mid 
                # Search the upper half
                low = mid + 1
        return low
            