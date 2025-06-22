class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxes = 0
        incomeLeft = income 

        for i in range(len(brackets)):
            if i == 0:
                toBeTaxed = min(brackets[i][0], incomeLeft)
            else:
                toBeTaxed = min(brackets[i][0] - brackets[i-1][0], incomeLeft)
            
            taxes += toBeTaxed * (brackets[i][1] / 100)
            incomeLeft -= toBeTaxed
        
        return taxes



