class Solution:
    def binary_search(self, left: int, right: int, nums: List[int], target: int) -> int:
        if left > right:
            return -1
        mid = left + ((right - left) // 2)

        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.binary_search(left, mid - 1, nums, target)
        return self.binary_search(mid + 1, right, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)