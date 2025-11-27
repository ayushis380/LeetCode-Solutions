class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = []
        dp = defaultdict(int)

        def findPower(n):
            if n in dp:
                return dp[n]
            
            if n == 1:
                return 0
            if n % 2:
                dp[n] = 1 + findPower(n * 3 + 1)
            else:
                dp[n] = 1 + findPower(n//2)
            
            return dp[n]
        
        for n in range(lo, hi + 1):
            value = findPower(n)
            power.append([value, n])
        
        power.sort(key = lambda x: (x[0], x[1]))

        return power[k-1][1]