class HitCounter:

    def __init__(self):
        self.hitmap = deque() # ( ts, number of hits)
        self.total = 0

    def hit(self, timestamp: int) -> None:
        if self.hitmap and self.hitmap[-1][0] == timestamp:
            self.hitmap[-1] = (timestamp, self.hitmap[-1][1] + 1)
        else:
            self.hitmap.append((timestamp, 1))
        
        self.total += 1
        self._cleanup(timestamp)
    
    def _cleanup(self, timestamp):
        while self.hitmap and self.hitmap[0][0] <= timestamp - 300:
            old_ts, count = self.hitmap.popleft()
            self.total -= count

    def getHits(self, timestamp: int) -> int:
        self._cleanup(timestamp)
        return self.total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)