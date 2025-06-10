class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#  Python, on the other hand, uses TimSort, which is a hybrid of MergeSort and InsertionSort and requires O(N) extra space. 
        heap = [] # max heap
        closest = []
        
        for x, y in points:
# simplify the process of comparing two points by using the squared Euclidean distance instead of the precise Euclidean distance, as both will yield the same result
# significantly reduce the overall computational time for each comparison made
            dist = -1 * (x ** 2 + y ** 2)
            heapq.heappush(heap, (dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            dist, x, y = heapq.heappop(heap)
            closest.append([x, y])
        
        return closest

        
