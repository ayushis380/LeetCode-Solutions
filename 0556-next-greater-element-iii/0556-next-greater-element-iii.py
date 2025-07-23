class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = list(str(n))
        length = len(num)

        i = length -2 # first smallest from end
        while i >= 0 and num[i] >= num[i+1]:
            i -= 1
        
        if i < 0:
            return -1
        
        j = length - 1 # just greater than value at num[i]
        while num[j] <= num[i]:
            j -= 1
        
        num[j], num[i] = num[i], num[j]
        num[i+1:] = reversed(num[i+1:])
        result = int(''.join(num))

        return result if result <= 2 ** 31 - 1 else -1

