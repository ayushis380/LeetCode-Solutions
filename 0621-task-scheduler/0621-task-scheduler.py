class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        queue = deque()
        time = 0

        for val in freq.values():
            heapq.heappush(heap, -1 * val)
        
        while heap or queue:
            time += 1
            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1
                if cnt:
                    queue.append((cnt, time + n))
            
            if queue and time == queue[0][1]:
                count, t = queue.popleft()
                heapq.heappush(heap, count)
        
        return time

