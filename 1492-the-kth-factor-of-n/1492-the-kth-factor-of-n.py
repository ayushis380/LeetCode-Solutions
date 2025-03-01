class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        n_sqrt = sqrt(n)
        factors = set()
        
        for i in range(1, int(n_sqrt) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n//i)
        
        if len(factors) < k:
            return -1
        
        return sorted(list(factors))[k-1]
        

