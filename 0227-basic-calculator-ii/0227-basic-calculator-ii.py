class Solution:
    def calculate(self, s: str) -> int:
        prev = "+"
        stack = []
        num = 0

        for i in range(0, len(s) + 1):
            ch = s[i] if i < len(s) else '\0'

            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if not ch.isdigit() and ch != " " or ch == "\0":
                if prev == "+":
                    stack.append(num)
                elif prev == "-":
                    stack.append(-num)
                elif prev == "*":
                    stack.append(stack.pop() * num)
                elif prev == "/":
                    stack.append(int(stack.pop() /num))
                
                prev = ch
                num = 0
        
        return sum(stack)
