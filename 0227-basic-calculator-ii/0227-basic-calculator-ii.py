class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        prev_op = '+' # to start as addition and subtraction have low priority 
        num = 0

# when at last index - we havent done the last operation seen
# so go till +1 to do that operation
# we do the operation once we have enough digits to perform that operation

        for i in range(len(s) + 1): # go +1 as to process the last operation 
            ch = s[i] if i < len(s) else '\0' # '\0' is taken as it doesnt match digits and ops

            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if not ch.isdigit() and ch != ' ' or i == len(s):
                if prev_op == "+":
                    stack.append(num)
                elif prev_op == "-":
                    stack.append(-num)
                elif prev_op == "*":
                    stack.append(stack.pop() * num)
                elif prev_op == "/":
                    stack.append(int(stack.pop() / num))
                
                prev_op = ch # in next iteration - do this operation
                num = 0
        
        return sum(stack)
