class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjlist = {ch: set() for wrd in words for ch in wrd}
        n = len(words)
        indegree = {ch: 0 for ch in adjlist}

        for i in range(n - 1):
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            
            for k in range(minlen):
                if w1[k] != w2[k]:
                    if w2[k] not in adjlist[w1[k]]: # if already in adjlist then dont add again, otherwise indegree will have extra values
                        adjlist[w1[k]].add(w2[k])
                        indegree[w2[k]] += 1
                    break # break once we get non matching chars
        
        queue = deque([ch for ch, cnt in indegree.items() if cnt == 0])
        result = ""

        while queue:
            ch = queue.popleft()
            result += ch

            for nei in adjlist[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return result if len(result) == len(adjlist) else ""