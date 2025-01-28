class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1

        for i in range(32):
            if (n & mask) != 0: # a logical AND between any number and the mask 1 gives us the least significant bit of this number.
                bits += 1
            
            mask <<= 1 # keep shifting to left, * 2 each time
            print(mask)
        
        return bits