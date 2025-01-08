class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapify(heap)
        queue = deque()

        time = 0
        while queue or heap:
            time += 1
            if heap:
                freq = heapq.heappop(heap)
                freq += 1 # freq is negative
                if freq: # if freq is 0 that means this char is complete
                    queue.append((freq, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        
        return time


