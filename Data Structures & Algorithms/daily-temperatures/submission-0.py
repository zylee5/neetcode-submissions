class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                i, tmp = stack.pop()
                days = idx - i
                res[i] = days
            stack.append((idx, temp))
        
        return res