class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # mid in the smaller portion
                # min is mid or to its left
                right = mid
            else:
                # mid in the larger portion
                # min is strictly to the right of mid
                left = mid + 1
        
        # min when left == right
        return nums[left]
                