class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find a meeting point inside the cycle
        slow1, fast = 0, 0
        while True:
            slow1 = nums[slow1]
            fast = nums[nums[fast]]
            if slow1 == fast:
                break
        
        # Find the cycle entrance
        slow2 = 0
        while True:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
            if slow1 == slow2:
                return slow1
        
        return -1
