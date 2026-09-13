class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # indices of elements with values large -> small
        res = []
        left = 0

        for right in range(len(nums)):
            # add right element to the window
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop() # remove indices of elements that are smaller than the new element
            queue.append(right)

            # remove index of largest element that is out of window
            if left > queue[0]:
                queue.popleft()
            
            # valid window size
            if right >= k - 1:
                # index of largest element is in the front of queue
                res.append(nums[queue[0]])
                left += 1
        
        return res
