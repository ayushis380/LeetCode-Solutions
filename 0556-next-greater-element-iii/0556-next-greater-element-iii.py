class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)

        i = length - 2
        while i >=0 and digits[i] >= digits[i+1]: # find the smallest value from end as replacing it will give next greater value
            i -= 1
        
        if i == -1:
            return -1 # number is the highest value that can be formed from digits, so return -1
        
        j = length - 1 # start from end
        while digits[j] <= digits[i]: # till we find a value just greater than smallest value found
            j -= 1
        digits[i], digits[j] = digits[j], digits[i] # swap

        digits[i+1:] = sorted(digits[i+1:]) # next perm
        result = int("".join(digits)) # digits is a list

        return result if result <= 2**31 - 1 else -1 
