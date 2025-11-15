class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        n= len(nums)
        arr = [[] * (n + 1) for _ in range(n + 1)] # [1], n = 1, n + 1 = 2 (0, 1) 
        freq = Counter(nums)

        for key, count in freq.items():
            arr[count].append(key)
        
        # for i in reversed(range(n + 1)): # n + 1 = 1+ 1 = 2, range(0, 2) = 1, 0
        #     print(i)

        for i in reversed(range(n + 1)): 
            for val in arr[i]:
                result.append(val)
            
            if len(result) == k:
                return result