class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(N) TC better than heap (N logk)
        freq = Counter(nums)
        topk = []
        arr = [[] for i in range(len(nums) + 1)]

        for key, count in freq.items():
            arr[count].append(key)
        
        for i in range(len(arr) -1, 0, -1):
            for val in arr[i]:
                topk.append(val)
            
            if len(topk) == k:
                return topk

            

        
