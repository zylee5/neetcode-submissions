class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # find pivot (index of smallest element)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        pivot = left
        
        left, right = 0, len(nums) - 1
        
        # find which sorted portion to search
        if nums[pivot] <= target and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1
        
        # standard binary search
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1