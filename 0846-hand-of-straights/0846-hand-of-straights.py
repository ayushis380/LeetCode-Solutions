class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        freq = Counter(hand)
        heap = list(freq.keys())
        heapq.heapify(heap)

        while heap:
            val = heap[0]
            for i in range(val, val + groupSize):
                if i not in freq:
                    return False
                
                freq[i] -= 1
                if freq[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        
        return True