class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        output = []
        freq = Counter(words)
        heap = []

        for word, count in enumerate(freq):
            heapq.heappush(heap, (count, word))

            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            word = heapq.heappop(heap)
            output.append(word)
        
        sort(output)
        return output