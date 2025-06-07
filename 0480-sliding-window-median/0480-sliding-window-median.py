class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo = [] # max heap whose size can be just +1 greater than hi
        hi = [] # min heap
        track = defaultdict(int)
        medians = []

        def get_median():
            if k%2: # when k is odd
                return float(-lo[0])
            else:
                return (-lo[0] + hi[0]) / 2

        # first k elements, lo can have just 1 element extra than hi
        for i in range(k):
            heapq.heappush(lo, -nums[i])
        
        for i in range(k//2):
            heapq.heappush(hi, -heapq.heappop(lo))
        
        # process next k elements
        i = k
        while True:
            medians.append(get_median())

            if i == len(nums):
                break
            
            out_num = nums[i-k]
            in_num = nums[i]
            i += 1
            balance = 0

            # outgoing element
            track[out_num] += 1
            if out_num <= -lo[0]: # lying on the left side means its in lo, max heap
                balance -= 1 # that means it will be removed from lo
            else:
                balance += 1 # otherwise removed from hi
            
            # incoming
            if in_num <= -lo[0]:
                heapq.heappush(lo, -in_num)
                balance += 1
            else:
                heapq.heappush(hi, in_num)
                balance -= 1
    
    # when we are talking about keeping the heaps balanced, the actual sizes of the heaps are irrelevant. Only the count of valid elements in both heaps matter.
#     balance =0: Both heaps are balanced or nearly balanced.
# balance <0: lo needs more valid elements. Elements from hi are moved to lo.
# balance >0: hi needs more valid elements. Elements from lo are moved to hi
            # rebalance 
            if balance < 0:
                heapq.heappush(lo, -heapq.heappop(hi))
                balance += 1
            
            if balance > 0:
                heapq.heappush(hi, -heapq.heappop(lo))
                balance -= 1
            
            # clean invalid : reach the heap tops, we remove them from the heaps
            while lo and track[-lo[0]]:
                track[-lo[0]] -= 1
                heapq.heappop(lo)
            
            while hi and track[hi[0]]:
                track[hi[0]] -= 1
                heapq.heappop(hi)
        
        return medians