class Solution:
    def maxPalindromes(self, S: str, k: int) -> int:
        N, intervals, last, ans = len(S), [], -inf, 0

        # to get all palindromes of size k
        for center in range(2 * N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                if right + 1 - left >= k: 
                    intervals.append((left, right + 1)) # next palindrome should start from right + 1 for non overl
                    break
                left -= 1
                right += 1
        
        print(intervals)
        
        for x, y in intervals:
            if x >= last: # if start of new palindrome >= end of last palindrome 
                last = y # update where this palindrome ends
                ans += 1
            else:
                if y < last: last = y # if overlap then take the smaller end value to make it non overlap, like done in intervals ques
        return ans