class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        result = []
        while start < end:
            twoSum = numbers[start] + numbers[end]
            if twoSum == target:
                result.extend([start + 1, end + 1])
                return result
            
            if twoSum < target:
                start += 1
            elif twoSum > target:
                end -= 1

        return result
