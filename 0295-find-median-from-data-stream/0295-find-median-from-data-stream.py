class MedianFinder:

    def __init__(self):
        # first half with smaller values: using maxheap
        # second half with larger values: using minheap
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        # add to one of the halves
        if self.large and num > self.large[0]: # comparing with large, no -1 multiplication req
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        # adjust the length of halves, one half can only be greater by 1 in len
        # dont forget to multiply by -1 for maxheap
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


    def findMedian(self) -> float:
        # first two conditions when heaps are unequal in size 
        # then median lies in middle, which will be on the longer half
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.small) < len(self.large):
            return self.large[0]
        # when even length, then add two mid elements
        else:
            return (-1 * self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()