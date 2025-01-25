class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # to store int
        
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                fval = stack.pop()
                sval = stack.pop()
                stack.append(sval - fval)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                fval = stack.pop()
                sval = stack.pop()
                stack.append(int(sval/fval))
            else:
                stack.append(int(t))
        
        return stack[-1]