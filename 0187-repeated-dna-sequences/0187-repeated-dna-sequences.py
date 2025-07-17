class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        seen = set()
        result = set()

        for i in range(n - 9):
            seq = s[i: i+10]
            if seq in seen:
                result.add(seq)
            
            seen.add(seq)
        
        return list(result)