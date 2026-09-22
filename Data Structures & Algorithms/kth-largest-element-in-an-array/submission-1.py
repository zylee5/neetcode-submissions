class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            pivotIdx = r
            pivot = nums[pivotIdx]
            i = l
            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i
        
        N = len(nums)
        l, r = 0, N - 1
        pivotIdx = -1
        while pivotIdx != N - k:
            pivotIdx = partition(l, r)
            if pivotIdx > N - k:
                r = pivotIdx - 1
            elif pivotIdx < N - k:
                l = pivotIdx + 1
        return nums[pivotIdx]