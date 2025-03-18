class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = defaultdict(list)

        for i, wrd in enumerate(wordsDict):
            self.words[wrd].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        # two pointer approach - these lists are already in sorted order - take benefit of that
        loc1 = self.words[word1]
        loc2 = self.words[word2]
        minDist = float("inf")
        l1, l2 = 0, 0 # two pointers
        
        while l1 < len(loc1) and l2 < len(loc2):
            minDist = min(minDist, abs(loc1[l1] - loc2[l2]))

            if loc1[l1] < loc2[l2]: # means there is no point in moving the l2 pointer forward as that would lead to a bigger difference - happens as lists have indexes in sorted order
                l1 += 1 # we increase l1 in hope of a better distance
            else:
                l2 += 1
        
        return minDist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)