from collections import deque

class HitCounter:
# that all the timestamps that we will encounter are going to be in increasing order
# we have to ignore the timestamps that occurred previously (having a difference of 300 or more with the latest timestamp)
    def __init__(self):
        self.hits = deque()  # stores (timestamp, count)
        self.total = 0       # running total of hits in the last 300 seconds

    def hit(self, timestamp: int) -> None:
        # If the last timestamp is the same, just update count
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1] = (timestamp, self.hits[-1][1] + 1)
        else:
            self.hits.append((timestamp, 1))

        self.total += 1
        self._cleanup(timestamp)

    def getHits(self, timestamp: int) -> int:
        self._cleanup(timestamp)
        return self.total

    def _cleanup(self, timestamp: int) -> None:
        # Remove all entries older than 300 seconds
        while self.hits and self.hits[0][0] <= timestamp - 300:
            old_timestamp, count = self.hits.popleft()
            self.total -= count
