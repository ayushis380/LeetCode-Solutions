class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # we don't need to compare every word to all of the words to its right
        # just compare each pair of adjacent words

        order_map = {}
        for index, ch in enumerate(order):
            order_map[ch] = index
        
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
# If we do not find a mismatch letter between words[i] and words[i + 1],
# we need to examine the case when words are like ("apple", "app").
                if j >= len(words[i+1]):
                    return False

# if we find the first different character and they are sorted,
# then there's no need to check remaining letters              
                if words[i][j] != words[i+1][j]:
                    if order_map[words[i][j]] > order_map[words[i+1][j]]:
                        return False
                
                    break

        return True

