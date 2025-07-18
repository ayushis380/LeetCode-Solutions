class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxes = 0
        prev = 0

        for upper, per in brackets:
            upper = min(upper, income)
            taxes += (upper - prev) * (per/100)
            prev = upper
        
        return taxes