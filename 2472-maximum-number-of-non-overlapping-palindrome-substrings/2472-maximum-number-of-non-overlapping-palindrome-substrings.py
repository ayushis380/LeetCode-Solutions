class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def palindrome(low, high):
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if (high - low + 1) >= k:
                    ranges.append([low, high + 1])
                    break
                low -= 1
                high += 1

        ranges = []
        n = len(s)

        for i in range(len(s)):
            palindrome(i, i)
            palindrome(i, i + 1)

        ranges.sort(key = lambda x: x[1])
        store = []
        for s, e in ranges:
            if not store or s > store[-1][1]:
                store.append([s, e])
        
        return len(store)