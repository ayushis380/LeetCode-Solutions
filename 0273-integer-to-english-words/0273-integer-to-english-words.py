class Solution:
    def __init__(self):
        self.less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.big = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return self.less_than_20[num] + " "
            elif num < 100:
                return self.tens[num // 10] + " " + helper(num % 10)
            else:
                return self.less_than_20[num // 100] + " Hundred " + helper(num % 100)

        res = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + self.big[i] + " " + res
            num //= 1000
            i += 1

        return res.strip()

# Example usage
solution = Solution()
print(solution.numberToWords(1234567))  # Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
