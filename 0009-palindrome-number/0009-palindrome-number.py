class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): # negative and which have 0 at end - wont be palind(except 0)
            return False
        
        rev = 0

        while x > rev: # only take the first half to compare with second half
            rev = rev * 10 + x % 10
            x = x//10 # O(log (base10(n)) - as /10 at each step
        
        # print("x is ", x, " rev is ", rev)
        return x == rev or x == rev//10 # 12321 - here rev will be 123, odd length can drop the middle element