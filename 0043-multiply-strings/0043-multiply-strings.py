class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        n1, n2 = num1[::-1], num2[::-1]
        res = [0] * (m + n) # product will have at max these many chars

        for i in range(m):
            for j in range(n):
                mult = int(n1[i]) * int(n2[j])
                res[i+j] += mult
                res[i+j+ 1] += res[i+j] // 10 # carry to next position
                res[i + j] = res[i+j] % 10 # mod at curr pos
        
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)

        


        
