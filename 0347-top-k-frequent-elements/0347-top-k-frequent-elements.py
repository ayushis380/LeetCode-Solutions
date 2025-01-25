class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # arr = [[]] * (len(nums) + 1) # creates a list where each element is a reference to the same list object, so when u update any list it will update all
        arr = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)
        topk = []

        for key, freq in count.items():
            arr[freq].append(key)

        for i in range(len(arr) - 1, 0, -1):
            for val in arr[i]:
                topk.append(val)
                if len(topk) == k:
                    return topk
        