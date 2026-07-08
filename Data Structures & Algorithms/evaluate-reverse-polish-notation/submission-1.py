class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        

        total = 0
        for token in tokens:
            if token == "+":
                a, b = stack.pop(), stack.pop()
                res = b + a
                
                stack.append(res)
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                res = b - a
                stack.append(res)
            elif token == "*":
                a, b = stack.pop(), stack.pop()
                res = b * a
                stack.append(res)
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                res = b / a
                stack.append(int(res))
            else: 
                stack.append(int(token))

        return stack[-1]
