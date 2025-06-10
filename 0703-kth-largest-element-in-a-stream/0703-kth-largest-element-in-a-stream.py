class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
# keeping track of just the k largest elements allows us to efficiently maintain the k-th largest element
# If an incoming element val is smaller than or equal to the existing k-th largest element: The k largest elements remain unchanged, and we can return the current k-th largest element.
# If val is larger than the current k-th largest element: It replaces the current k-th largest element. After adding val, the new k-th largest element is the next largest element.
        for score in nums:
            self.add(score)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
                heapq.heappop(self.heap)
        
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)