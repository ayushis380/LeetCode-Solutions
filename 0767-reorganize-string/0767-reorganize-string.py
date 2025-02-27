class Solution:
    def reorganizeString(self, s: str) -> str:
        result = []
        count = Counter(s)

        heap = [(-1 * cnt, ch) for ch, cnt in count.items()]
        heapq.heapify(heap)

        while heap:
            cnt_first, ch_first = heapq.heappop(heap)

            if not result or result[-1] != ch_first:
                result.append(ch_first)
                if (cnt_first + 1):
                    heapq.heappush(heap, (cnt_first + 1, ch_first))
            else:
                if not heap:
                    return ""
                
                cnt_second, ch_second = heapq.heappop(heap)
                result.append(ch_second)
                if (cnt_second + 1):
                    heapq.heappush(heap, (cnt_second + 1, ch_second))
                
                heapq.heappush(heap, (cnt_first, ch_first))
        
        return "".join(result)