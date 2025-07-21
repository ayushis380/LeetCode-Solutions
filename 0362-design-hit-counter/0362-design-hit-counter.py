class HitCounter:

    def __init__(self):
        self.queue = deque()
        self.total = 0 

    def hit(self, timestamp: int) -> None:
        if self.queue and self.queue[-1][0] == timestamp:
            self.queue[-1][1] += 1
        else:
            self.queue.append([timestamp, 1])
        
        self.total += 1 # each hit, add to total
        self._cleanup(timestamp)

    def getHits(self, timestamp: int) -> int:
        self._cleanup(timestamp)
        return self.total
    
    def _cleanup(self, timestamp):
        while self.queue and self.queue[0][0] <= timestamp - 300:
            ts, count = self.queue.popleft()
            self.total -= count
        
        return self.total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)