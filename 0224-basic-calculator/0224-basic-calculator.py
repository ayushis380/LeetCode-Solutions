class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "+":
                res += sign * num
                sign = 1
                num = 0
            elif ch == "-":
                res += sign * num
                sign = -1
                num = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)

                res = 0
                sign = 1
            elif ch == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()

                num = 0
        
        return res + sign * num