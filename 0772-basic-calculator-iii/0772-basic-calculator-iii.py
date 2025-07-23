class Solution:
    def calculate(self, s: str) -> int:
        def helper(it):
            stack = []
            prev = "+"
            num = 0

            while it < len(s):
                ch = s[it]
                if ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch == '(':
                    it, num = helper(it + 1)
                
                if not ch.isdigit() or it == len(s) - 1:
                    if prev == "+":
                        stack.append(num)
                    elif prev == "-":
                        stack.append(-num)
                    elif prev == "*":
                        stack.append(num * stack.pop())
                    elif prev == "/":
                        stack.append(int(stack.pop()/ num))
                    
                    num = 0
                    prev = ch

                    if ch == ')':
                        return it, sum(stack)
                
                it += 1
            
            return it, sum(stack)
        
        return helper(0)[1]



        