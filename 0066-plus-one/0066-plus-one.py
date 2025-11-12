class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        n = len(digits)
        carry = 0
        total = 0

        for i in reversed(range(n)):
            total = carry + digits[i]
            if i == n -1:
                total += 1
            
            result.append(total % 10)
            carry = total// 10
        
        if carry > 0:
            result.append(carry)
        
        return result[::-1]