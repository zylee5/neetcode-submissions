class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        minSpeed = right

        while left <= right:
            speed = (right + left) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            if hours <= h:
                minSpeed = speed
                # Continue searching left half (potential lower speed)
                right = speed - 1
            else:
                left = speed + 1
        
        return minSpeed