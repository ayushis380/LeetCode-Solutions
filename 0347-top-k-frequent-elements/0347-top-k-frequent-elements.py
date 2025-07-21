class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        result = []
        arr = [[] for i in range(len(nums) + 1)]

        for n, count in freq.items():
            arr[count].append(n)

        for j in range(len(arr) - 1, 0, -1):
            for val in arr[j]:
                result.append(val)
            
            if len(result) == k:
                return result
