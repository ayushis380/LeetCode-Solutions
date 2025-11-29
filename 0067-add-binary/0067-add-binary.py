class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # XOR + AND = Binary Addition
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1 # carry affects the NEXT bit, so we left-shift it
            # print("answer is ", answer)
            # print("carry is ", carry)
            x, y = answer, carry
        
        return bin(x)[2:] # always gives 0b1010, so slice