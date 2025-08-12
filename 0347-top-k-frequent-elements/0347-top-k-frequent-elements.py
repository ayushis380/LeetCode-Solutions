class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = [[] for i in range(len(nums) + 1)]
        topk = []
        
        for n, fre in count.items():
            arr[fre].append(n)
        
        for i in range(len(arr) - 1, -1, -1):
            for val in arr[i]:
                topk.append(val)
            
            if len(topk) == k:
                return topk