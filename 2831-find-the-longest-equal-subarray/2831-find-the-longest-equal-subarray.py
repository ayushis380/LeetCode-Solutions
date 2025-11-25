class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        ind = defaultdict(list)
        maxlen = 0

        for i, n in enumerate(nums):
            ind[n].append(i)
        
        for n, ls in ind.items():
            l = 0
            length = len(ls)

            for r in range(length):
                while ls[r] - ls[l] - (r - l) > k:
                    l += 1

                maxlen = max(maxlen, r - l + 1)

        return maxlen 