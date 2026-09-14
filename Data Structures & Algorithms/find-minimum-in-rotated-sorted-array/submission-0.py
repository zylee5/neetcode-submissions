class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = nums[0]

        while left <= right:
            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                # [left, mid] is in the larger portion
                # min is in the smaller portion that is to the right
                left = mid + 1
            else:
                # [left, mid] contains larger and smaller portion
                # min must be midpoint or in the smaller portion that is to the left
                # portion to the right must be larger than midpoint, so no search
                right = mid - 1
                res = min(res, nums[mid])
        
        return res