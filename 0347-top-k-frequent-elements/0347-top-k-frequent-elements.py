class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [] # min heap 
        freq = Counter(nums)
        result = []

        for n, count in freq.items():
            heapq.heappush(heap, (count, n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            ct, num = heapq.heappop(heap)
            result.append(num)
        
        return result