class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                second = float(stack.pop())
                first = float(stack.pop())

                if token == '+':
                    result = first + second
                elif token == '-':
                    result = first - second
                elif token == '*':
                    result = first * second
                elif token == '/':
                    result = first / second
                stack.append(str(int(result)))
            else:
                stack.append(token)

        return int(stack[-1]) if stack else 0