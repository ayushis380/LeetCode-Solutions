class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.scores = []
        
        for score in nums:
            if len(self.scores) < k:
                heapq.heappush(self.scores, score)
            elif self.scores[0] < score:
                heapq.heappushpop(self.scores, score)

    def add(self, val: int) -> int:

        if len(self.scores) < self.k:
            heapq.heappush(self.scores, val)
        elif self.scores[0] < val:
            heapq.heappushpop(self.scores, val)
        
        return self.scores[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)