class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        minHeap = []
        result = []
        for key, value in freq.items():
            if len(minHeap) < k:
                heapq.heappush(minHeap, (value, key))
            elif value > minHeap[0][0]:
                heapq.heappushpop(minHeap, (value, key))
        for i in range(len(minHeap)):
            result.append(heapq.heappop(minHeap)[1])
        return result