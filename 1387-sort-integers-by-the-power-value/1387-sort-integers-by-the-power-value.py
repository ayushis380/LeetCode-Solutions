class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = []

        def findPower(n):
            if n == 1:
                return 0
            if n % 2:
                return 1 + findPower(n * 3 + 1)
            else:
                return 1 + findPower(n//2)
        
        for n in range(lo, hi + 1):
            value = findPower(n)
            power.append([value, n])
        
        power.sort(key = lambda x: (x[0], x[1]))

        return power[k-1][1]