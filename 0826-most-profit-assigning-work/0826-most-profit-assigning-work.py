class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        jobs = sorted(zip(difficulty, profit)) # nlog n

        max_profit_so_far = 0
        max_profits = []
        difficulties = []
        total_profit = 0

        for d, p in jobs:
            max_profit_so_far = max(max_profit_so_far, p)
            difficulties.append(d)
            max_profits.append(max_profit_so_far)
        
        for w in worker:
            # m log n : m workers, log n for binary search
            idx = bisect.bisect_right(difficulties, w) -1 # difficulties has sorted values of difficulty
            if idx >= 0:
                total_profit += max_profits[idx]
        
        return total_profit