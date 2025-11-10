class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    # BFS to find shortest path 
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        wordList.append(beginWord) # its not there in dictionary, we need it to find patterns
        queue = deque([beginWord])
        length = 1 # we already have beginWord to start from 
        visited = set([beginWord])

        # create patterns eg, hot has *ot, h*t, ho*. These will be the keys 
        # we choose this as only one key can be different 
        # words having same pattern will be connected, so its like building adjacency list of the graph
        # notice each pattern can have multiple values so when accessing them we need to make sure the visited condition is not met, otherwise the popped word and word in adj can be same
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:] # skip char at j and add * in place
                adj[pattern].append(word)
        
        while queue:
            curlen = len(queue)
            for i in range(curlen):
                word = queue.popleft()

                if word == endWord: # reached word
                    return length

                for j in range(len(word)): # check for all neighbors of the popped word
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            
            length += 1
        
        return 0


