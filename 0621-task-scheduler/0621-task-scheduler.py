class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0

        while heap or queue:
            time += 1
            
            if heap:
                ct = heapq.heappop(heap)
                ct += 1
                if ct:
                    queue.append((time + n, ct))
            
            if queue and queue[0][0] == time:
                curtime, count = queue.popleft()
                heapq.heappush(heap, count)
        
        return time



