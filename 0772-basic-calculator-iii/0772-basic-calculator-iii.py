class Solution:
    def calculate(self, s: str) -> int:
        def helper(it):
            stack = []
            num = 0
            prev_op = "+"

            while it < len(s):
                ch = s[it]

                if ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch == '(':
                    it, num = helper(it + 1)
                    
                # it == len(s) - 1) → you're out of characters, so do the pending operation with num.
                if not ch.isdigit() or it == len(s) - 1 or ch == ')':
                    if prev_op == '+':
                        stack.append(num)
                    elif prev_op == '-':
                        stack.append(-num)
                    elif prev_op == '*':
                        stack.append(stack.pop() * num)
                    elif prev_op == '/':
                        stack.append(int(stack.pop() / num))
                    
                    num = 0
                    prev_op = ch

                    if ch == ')':
                        return it, sum(stack)
                
                it += 1
            
            return it, sum(stack)
        
        return helper(0)[1]

