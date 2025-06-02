class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord_map = {}

        for i, ch in enumerate(order):
            ord_map[ch] = i
        
        for i in range(len(words) - 1): # compare i and i+1 word, if all follow the rule then all are in order 
            for j in range(len(words[i])):
                
                if j >= len(words[i+1]):
                    return False
                
                if words[i][j] != words[i+1][j]:
                    if ord_map[words[i][j]] > ord_map[words[i+1][j]]:
                        return False
                    break
        
        return True