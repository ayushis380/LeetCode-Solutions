class Solution:
    def calculate(self, s: str) -> int:
        sign = 1 # 1 for positive, -1 for negative
        res = 0
        operand = 0
        stack = []

        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            elif ch == '+':
                res += sign * operand # existing sign and operand
                sign = 1
                operand = 0
            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == '(': 
                stack.append(res) # appending seen result 
                stack.append(sign)

                sign = 1
                res = 0 # start new result from ( bracket
            elif ch == ")":
                res += sign * operand # result in between ( ) these twp
                res *= stack.pop() # pop the old sign
                res += stack.pop() # pop the old result
                operand = 0
        
        return res + sign * operand # make sure last operand is evaluated because we evaluate left when we go to right - but for last operand the loop exists before
