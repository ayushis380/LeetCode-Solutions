class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def sum_of_digits(number):
            return sum(int(d) for d in str(number))
        
        if sum_of_digits(n) <= target:
            return 0
        
# when number is not beautiful we are looking for next valid n 
# "zero out" the lower digits from right to left — this is faster than trying every x
# 467 -> 470 -> 500 -> 1000, as sum of number from 467 to 469 will be greater than target
        multiplier = 1
        original = n

        while True:
            n = (n // multiplier + 1) * multiplier
            if sum_of_digits(n) <= target:
                return n - original
            
            multiplier *= 10 # next power of 10