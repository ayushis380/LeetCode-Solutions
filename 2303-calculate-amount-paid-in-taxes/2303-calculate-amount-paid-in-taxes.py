class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxes = 0
        total = 0

        for upper, per in brackets:
            amount = min(upper, income) - total
            taxes += (amount * per) /100
            total += amount
        
        return taxes