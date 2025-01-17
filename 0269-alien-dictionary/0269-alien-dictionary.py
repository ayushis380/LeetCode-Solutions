class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Kahns Algo: Topological sorting
        # build adj list and indegree
        adj = {c : set() for wrd in words for c in wrd}
        indegree = {c: 0 for c in adj}

        # build graph
        for i in range(len(words) - 1): # compare two words at a time
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
# words are lexicographically stored as per alien dictionary
# If w1 is longer than w2 but w2 is a prefix of w1, the order is invalid
# eg w1 = xbz, w2 = xb, then w2 should have come before w1
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
# we break after first mismatch
# The first mismatch between two adjacent words is enough to establish the relative order of two characters
# word1 = "wrtabc" and word2 = "wrfxyz", only 't' and 'f' matter because the alien dictionary order will never require comparing 'a' with 'x'
            for j in range(minlen):
                if w1[j] != w2[j]: # looking for first mismatch to update adj, indegree
                    if w2[j] not in adj[w1[j]]: # w1 char is before w2 char
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1 
                    break
        
        # updating queue 
        queue = deque([c for c in indegree if indegree[c] == 0]) # no dependency
        order = []
        while queue:
            char = queue.popleft()
            order.append(char)
            for nei in adj[char]:
                indegree[nei] -= 1 # as char is removed
                if indegree[nei] == 0: # add all neighbors which have no dependency
                    queue.append(nei)
        
        if len(order) != len(adj): # should have all characters
            return ""
        
        return "".join(order)

