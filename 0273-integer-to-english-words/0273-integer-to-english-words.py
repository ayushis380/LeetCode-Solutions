class Solution:
    def __init__(self):
        self.less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.big = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        def helper(num):
            if not num:
                return ""
            elif num < 20:
                return self.less_than_20[num] + " "
            elif num < 100:
                return self.tens[num // 10] + " " + helper(num % 10)
            else:
                return self.less_than_20[num // 100] + " Hundred " + helper(num % 100)
        
        result = ""
        i = 0 # dividing number into chunks of 3 
        
        while num > 0:
            if num % 1000 != 0:
                result = helper(num % 1000) + self.big[i] + " " + result
            
            num //= 1000
            i += 1
        
        return result.strip()


