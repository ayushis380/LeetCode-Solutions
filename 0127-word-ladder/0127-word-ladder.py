class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        queue = deque([beginWord])
        visited = set([(beginWord)])
        adjlist = defaultdict(list)
        steps = 1

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adjlist[pattern].append(word)
        
        while queue:
            curlen = len(queue)
            for _ in range(curlen):
                word = queue.popleft()
                if word == endWord:
                    return steps
                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in adjlist[pattern]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            
            steps += 1
        
        return 0

        