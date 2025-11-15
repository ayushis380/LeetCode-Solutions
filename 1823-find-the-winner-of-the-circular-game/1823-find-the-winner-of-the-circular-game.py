class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return self.winnerHelper(n, k) + 1

    def winnerHelper(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        return (self.winnerHelper(n - 1, k) + k) % n

# Iterative
        # ans = 0
        # for i in range(2, n + 1):
        #     ans = (ans + k) % i
        # # add 1 to convert back to 1 indexing
        # return ans + 1