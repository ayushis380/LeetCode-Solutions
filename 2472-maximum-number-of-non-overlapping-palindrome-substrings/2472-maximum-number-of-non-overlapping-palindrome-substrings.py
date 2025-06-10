class Solution:
    def maxPalindromes(self, S: str, k: int) -> int:
        N, ans, start = len(S), 0, 0
        
        for center in range(2 * N - 1):
        # Odd: center is even → left == right
        # Even: center is odd → right = left + 1
            # centre of palindrome, eg (0,0), (0,1), (1,1), (1,2)...
            left = center // 2 # center = even value eg 0, 2 then left == right 
            right = left + center % 2 # center = 3, 5 then left = 1, 2 and right is always left + 1
        
            while left >= start and right < N and S[left] == S[right]:
                if right + 1 - left >= k: # found a valid palindrome, dont expand if we get one
                    ans += 1
                    start = right + 1 # starts at or after start to prevent overlapping, next palindrome can start from right+1
                    break # stop expanding — move to next center
                left -= 1
                right += 1
        
        return ans