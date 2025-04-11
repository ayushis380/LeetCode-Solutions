class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        topk = []
        arr = [[] for i in range(len(nums) + 1)] # if any number appears that means it can't have 0 as count, so need an extra array at the end
        # mapping frequency of n to the index of arr

        for n, count in freq.items():
            arr[count].append(n)
        
        print(arr)
        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                topk.append(n)
            
            if len(topk) == k:
                return topk

