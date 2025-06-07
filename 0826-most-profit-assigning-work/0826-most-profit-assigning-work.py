import bisect
from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Step 1: Pair and sort jobs by difficulty
        jobs = sorted(zip(difficulty, profit))  # [(difficulty, profit)]
        
        # Step 2: Build prefix max profits for each difficulty
# A worker with skill level w can perform any job with difficulty ≤ w.
# But the job list might have: many jobs with same difficulty but lower profits, or easier jobs with higher profits than harder ones.
        
        max_profits = []
        max_profit_so_far = 0
        difficulties = []

        for d, p in jobs:
            max_profit_so_far = max(max_profit_so_far, p)  # Track the highest profit so far
            difficulties.append(d)                         # Store the difficulty
            max_profits.append(max_profit_so_far)          # Store the best profit up to this point
        
        # Step 3: For each worker, binary search the best difficulty <= their skill
        total_profit = 0
        for w in worker:
            idx = bisect.bisect_right(difficulties, w) - 1
            if idx >= 0:
                total_profit += max_profits[idx]  # Add best possible profit
        
        return total_profit
