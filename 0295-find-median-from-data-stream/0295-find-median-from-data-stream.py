class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -1 * num)
        
        if len(self.left) > len(self.right) + 1:
            val = heapq.heappop(self.left) * -1
            heapq.heappush(self.right, val)
        elif len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right) * -1
            heapq.heappush(self.left, val)
        

    def findMedian(self) -> float:
        total = len(self.left) + len(self.right)

        if total % 2: # odd
            if len(self.left) > len(self.right): # consider the bigger one, as its top element will be the median
                return -1 * self.left[0]
            else:
                return self.right[0]
        else:
            return (-1 * self.left[0] + self.right[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()