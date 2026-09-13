class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        pairMap = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif stack and (pairMap.get(char) == stack[-1]):
                stack.pop()
            else:
                return False
        
        return len(stack) == 0