class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        pivot = 0 # index of the smallest element

        while left <= right:
            if nums[left] <= nums[right]:
                if nums[left] < nums[pivot]:
                    pivot = left
                break
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
                if nums[mid] < nums[pivot]:
                    pivot = mid
        
        left, right = 0, len(nums) - 1
        if nums[pivot] <= target and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
