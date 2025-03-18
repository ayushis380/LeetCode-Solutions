# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        degree = [0] * n

        for i in range(n):
            for j in range(i+1, n):
                if knows(i, j):
                    degree[j] += 1
                    degree[i] -= 1
                if knows(j, i):
                    degree[i] += 1
                    degree[j] -= 1
        
        for ind, dgr in enumerate(degree):
            if dgr == (n-1):
                return ind
        
        return -1