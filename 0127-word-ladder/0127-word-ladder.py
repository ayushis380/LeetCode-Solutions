class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        adjlist = defaultdict(list)
        queue = deque([beginWord])
        steps = 1
        visited = set([beginWord])

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adjlist[pattern].append(word)
        
        while queue:
            curlen = len(queue)

            for i in range(curlen):
                word = queue.popleft()
                
                if word == endWord:
                    return steps

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adjlist[pattern]:
                        if nei not in visited: # neighbors are the words which have same pattern
                            queue.append(nei)
                            visited.add(nei)

            steps += 1 # increment when done full step - we might not need to increase if condition matches already

        return 0
