class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)
        # bucket[weight] = number of stones with that weight
        for stone in stones:
            bucket[stone] += 1
        
        first = second = maxStone
        while first > 0:
            # stones of the same weight cancel out in pairs
            # if the count is even, none of this weight remain
            if bucket[first] % 2 == 0:
                first -= 1
                continue
            
            # an odd count means one stone of this weight remains
            # find the next heaviest remaining stone
            j = min(first - 1, second)
            while j > 0 and bucket[j] == 0:
                j -= 1
            if j == 0:
                return first
            second = j

            # smash the two heaviest stones
            # remove one of each and add their weight difference
            diff = first - second
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[diff] += 1

            first = max(diff, second)
        
        return first