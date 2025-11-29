class Solution:
    def romanToInt(self, s: str) -> int:
        num = {
            "M" : 1000,
            "CM": 900,
            "D" : 500,
            "CD" : 400,
            "C" : 100,
            "XC" : 90,
            "L" : 50,
            "XL" : 40,
            "X": 10,
            "IX" : 9,
            "V" : 5,
            "IV" : 4,
            "I" : 1
        }

        n = len(s)
        total = 0
        i = 0
        while i < n:
            if i + 1 < n and num[s[i]] < num[s[i+1]]:
                total += num[s[i: i+2]]
                i += 2
            else:
                total += num[s[i]]
                i += 1
        
        return total