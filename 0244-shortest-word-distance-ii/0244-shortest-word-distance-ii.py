class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        self.words = defaultdict(list)

        for i, wrd in enumerate(self.wordsDict):
            self.words[wrd].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        l1 = self.words[word1]
        l2 = self.words[word2]
        minDist = len(self.wordsDict)

        for i in l1:
            for j in l2:
                minDist = min(minDist, abs(i - j))
        
        return minDist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)