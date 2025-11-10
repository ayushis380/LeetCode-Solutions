class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        length = 1
        wordList.append(beginWord)
        queue = deque([beginWord])
        adjlist = defaultdict(list)
        visited = set([beginWord])

        for wrd in wordList:
            for j in range(len(wrd)):
                pattern = wrd[:j] + "*" + wrd[j+1:]
                adjlist[pattern].append(wrd)
        
        while queue:
            curlen = len(queue)

            for _ in range(curlen):
                word = queue.popleft()
                if word == endWord:
                    return length
                visited.add(word)

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adjlist[pattern]:
                        if nei not in visited:
                            queue.append(nei)
            
            length += 1
